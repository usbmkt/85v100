#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ARQV30 Enhanced v2.0 - Unified Search Manager CORRIGIDO
Gerenciador unificado de busca com múltiplos provedores - FUNCIONANDO
"""

import os
import logging
import time
import requests
from typing import Dict, List, Optional, Any
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
import json
import random
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed

logger = logging.getLogger(__name__)

class UnifiedSearchManager:
    """Gerenciador unificado de busca com múltiplos provedores - CORRIGIDO"""

    def __init__(self):
        """Inicializa o gerenciador unificado"""
        self.google_search_key = os.getenv('GOOGLE_SEARCH_KEY')
        self.google_cse_id = os.getenv('GOOGLE_CSE_ID')
        self.serper_api_key = os.getenv('SERPER_API_KEY')
        self.jina_api_key = os.getenv('JINA_API_KEY')

        self.providers = {
            'google': {
                'enabled': bool(self.google_search_key and self.google_cse_id),
                'priority': 1,
                'error_count': 0,
                'max_errors': 3,
                'base_url': 'https://www.googleapis.com/customsearch/v1'
            },
            'serper': {
                'enabled': bool(self.serper_api_key),
                'priority': 2,
                'error_count': 0,
                'max_errors': 3,
                'base_url': 'https://google.serper.dev/search'
            },
            'bing': {
                'enabled': True,  # Sempre disponível via scraping
                'priority': 3,
                'error_count': 0,
                'max_errors': 5,
                'base_url': 'https://www.bing.com/search'
            },
            'duckduckgo': {
                'enabled': True,  # Sempre disponível via scraping
                'priority': 4,
                'error_count': 0,
                'max_errors': 5,
                'base_url': 'https://html.duckduckgo.com/html/'
            }
        }

        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'pt-BR,pt;q=0.9,en;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'DNT': '1',
            'Connection': 'keep-alive'
        }

        # Domínios brasileiros preferenciais
        self.preferred_domains = [
            "g1.globo.com", "exame.com", "valor.globo.com", "estadao.com.br",
            "folha.uol.com.br", "canaltech.com.br", "tecmundo.com.br",
            "olhardigital.com.br", "infomoney.com.br", "startse.com",
            "revistapegn.globo.com", "epocanegocios.globo.com", "istoedinheiro.com.br"
        ]

        enabled_count = sum(1 for p in self.providers.values() if p['enabled'])
        logger.info(f"🔍 Unified Search Manager CORRIGIDO inicializado com {enabled_count} provedores")

    def unified_search(
        self, 
        query: str, 
        max_results: int = 20,
        context: Dict[str, Any] = None,
        session_id: str = None
    ) -> Dict[str, Any]:
        """Realiza busca unificada FUNCIONAL com todos os provedores disponíveis"""

        logger.info(f"🔍 INICIANDO BUSCA REAL para: {query}")
        start_time = time.time()

        all_results = []
        provider_results = {}

        # Lista de buscas a serem executadas
        search_tasks = []

        # 1. Google Custom Search
        if self.providers['google']['enabled']:
            search_tasks.append(('google', self._search_google, query, max_results // 3))

        # 2. Serper API
        if self.providers['serper']['enabled']:
            search_tasks.append(('serper', self._search_serper, query, max_results // 3))

        # 3. Bing Scraping
        if self.providers['bing']['enabled']:
            search_tasks.append(('bing', self._search_bing, query, max_results // 4))

        # 4. DuckDuckGo Scraping
        if self.providers['duckduckgo']['enabled']:
            search_tasks.append(('duckduckgo', self._search_duckduckgo, query, max_results // 4))

        # Executa buscas em paralelo
        if search_tasks:
            with ThreadPoolExecutor(max_workers=4) as executor:
                future_to_provider = {}

                for provider_name, search_func, search_query, max_res in search_tasks:
                    future = executor.submit(search_func, search_query, max_res)
                    future_to_provider[future] = provider_name

                for future in as_completed(future_to_provider, timeout=45):
                    provider_name = future_to_provider[future]
                    try:
                        results = future.result()
                        if results:
                            all_results.extend(results)
                            provider_results[provider_name] = results
                            logger.info(f"✅ {provider_name}: {len(results)} resultados REAIS")
                        else:
                            logger.warning(f"⚠️ {provider_name}: 0 resultados")
                    except Exception as e:
                        logger.error(f"❌ Erro no {provider_name}: {e}")
                        self._record_provider_error(provider_name)

        # Remove duplicatas por URL
        unique_results = self._remove_duplicates(all_results)

        # Prioriza domínios brasileiros
        prioritized_results = self._prioritize_brazilian_sources(unique_results)

        # Calcula métricas
        search_time = time.time() - start_time

        unified_result = {
            'query': query,
            'context': context,
            'results': prioritized_results,
            'provider_results': provider_results,
            'statistics': {
                'total_results': len(prioritized_results),
                'providers_used': len(provider_results),
                'search_time': search_time,
                'brazilian_sources': sum(1 for r in prioritized_results if r.get('is_brazilian')),
                'preferred_sources': sum(1 for r in prioritized_results if r.get('is_preferred'))
            },
            'metadata': {
                'timestamp': datetime.now().isoformat(),
                'session_id': session_id,
                'search_type': 'unified_multi_provider_real'
            }
        }

        logger.info(f"✅ BUSCA REAL CONCLUÍDA: {len(prioritized_results)} resultados únicos em {search_time:.2f}s")

        return unified_result

    def _search_google(self, query: str, max_results: int) -> List[Dict[str, Any]]:
        """Busca REAL usando Google Custom Search API"""

        try:
            enhanced_query = self._enhance_query_for_brazil(query)

            params = {
                'key': self.google_search_key,
                'cx': self.google_cse_id,
                'q': enhanced_query,
                'num': min(max_results, 10),
                'lr': 'lang_pt',
                'gl': 'br',
                'safe': 'off',
                'dateRestrict': 'm12'
            }

            response = requests.get(
                self.providers['google']['base_url'],
                params=params,
                headers=self.headers,
                timeout=20
            )

            if response.status_code == 200:
                data = response.json()
                results = []

                for item in data.get('items', []):
                    results.append({
                        'title': item.get('title', ''),
                        'url': item.get('link', ''),
                        'snippet': item.get('snippet', ''),
                        'source': 'google_real'
                    })

                return results
            else:
                raise Exception(f"Google API retornou status {response.status_code}")

        except Exception as e:
            logger.error(f"❌ Erro Google Search: {e}")
            return []

    def _search_serper(self, query: str, max_results: int) -> List[Dict[str, Any]]:
        """Busca REAL usando Serper API"""

        try:
            enhanced_query = self._enhance_query_for_brazil(query)

            headers = {
                **self.headers,
                'X-API-KEY': self.serper_api_key,
                'Content-Type': 'application/json'
            }

            payload = {
                'q': enhanced_query,
                'gl': 'br',
                'hl': 'pt',
                'num': max_results
            }

            response = requests.post(
                self.providers['serper']['base_url'],
                json=payload,
                headers=headers,
                timeout=20
            )

            if response.status_code == 200:
                data = response.json()
                results = []

                for item in data.get('organic', []):
                    results.append({
                        'title': item.get('title', ''),
                        'url': item.get('link', ''),
                        'snippet': item.get('snippet', ''),
                        'source': 'serper_real'
                    })

                return results
            else:
                raise Exception(f"Serper API retornou status {response.status_code}")

        except Exception as e:
            logger.error(f"❌ Erro Serper Search: {e}")
            return []

    def _search_bing(self, query: str, max_results: int) -> List[Dict[str, Any]]:
        """Busca REAL usando Bing (webscraping)"""

        try:
            enhanced_query = self._enhance_query_for_brazil(query)
            search_url = f"{self.providers['bing']['base_url']}?q={quote_plus(enhanced_query)}&cc=br&setlang=pt-br&count={max_results}"

            response = requests.get(search_url, headers=self.headers, timeout=20)

            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                results = []

                result_items = soup.find_all('li', class_='b_algo')

                for item in result_items[:max_results]:
                    title_elem = item.find('h2')
                    if title_elem:
                        link_elem = title_elem.find('a')
                        if link_elem:
                            title = title_elem.get_text(strip=True)
                            url = link_elem.get('href', '')

                            snippet_elem = item.find('p')
                            snippet = snippet_elem.get_text(strip=True) if snippet_elem else ""

                            if url and title and url.startswith('http'):
                                results.append({
                                    'title': title,
                                    'url': url,
                                    'snippet': snippet,
                                    'source': 'bing_webscraping'
                                })

                return results
            else:
                raise Exception(f"Bing retornou status {response.status_code}")

        except Exception as e:
            logger.error(f"❌ Erro Bing Webscraping: {e}")
            return []

    def _search_duckduckgo(self, query: str, max_results: int) -> List[Dict[str, Any]]:
        """Busca REAL usando DuckDuckGo (webscraping)"""

        try:
            enhanced_query = self._enhance_query_for_brazil(query)
            search_url = f"{self.providers['duckduckgo']['base_url']}?q={quote_plus(enhanced_query)}"

            response = requests.get(search_url, headers=self.headers, timeout=20)

            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                results = []

                result_divs = soup.find_all('div', class_='result')

                for div in result_divs[:max_results]:
                    title_elem = div.find('a', class_='result__a')
                    snippet_elem = div.find('a', class_='result__snippet')

                    if title_elem:
                        title = title_elem.get_text(strip=True)
                        url = title_elem.get('href', '')
                        snippet = snippet_elem.get_text(strip=True) if snippet_elem else ""

                        if url and title and url.startswith('http'):
                            results.append({
                                'title': title,
                                'url': url,
                                'snippet': snippet,
                                'source': 'duckduckgo_webscraping'
                            })

                return results
            else:
                raise Exception(f"DuckDuckGo retornou status {response.status_code}")

        except Exception as e:
            logger.error(f"❌ Erro DuckDuckGo Webscraping: {e}")
            return []

    def _enhance_query_for_brazil(self, query: str) -> str:
        """Melhora query para pesquisa no Brasil"""

        enhanced_query = query
        query_lower = query.lower()

        # Adiciona termos brasileiros se não estiverem presentes
        if not any(term in query_lower for term in ["brasil", "brasileiro", "br"]):
            enhanced_query += " Brasil"

        # Adiciona ano atual se não estiver presente
        if not any(year in query for year in ["2024", "2025"]):
            enhanced_query += " 2024"

        return enhanced_query.strip()

    def _remove_duplicates(self, results: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Remove duplicatas baseado na URL"""

        seen_urls = set()
        unique_results = []

        for result in results:
            url = result.get('url', '')
            if url and url not in seen_urls:
                seen_urls.add(url)
                unique_results.append(result)

        return unique_results

    def _prioritize_brazilian_sources(self, results: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Prioriza fontes brasileiras"""

        for result in results:
            url = result.get('url', '')
            domain = url.split('/')[2] if len(url.split('/')) > 2 else ''

            # Marca se é fonte brasileira
            result['is_brazilian'] = (
                domain.endswith('.br') or 
                'brasil' in domain.lower() or
                any(pref in domain for pref in self.preferred_domains)
            )

            # Marca se é fonte preferencial
            result['is_preferred'] = any(pref in domain for pref in self.preferred_domains)

            # Calcula score de prioridade
            priority_score = 1.0

            if result['is_preferred']:
                priority_score += 3.0
            elif result['is_brazilian']:
                priority_score += 2.0

            result['priority_score'] = priority_score

        # Ordena por prioridade
        results.sort(key=lambda x: x.get('priority_score', 0), reverse=True)

        return results

    def _record_provider_error(self, provider_name: str):
        """Registra erro do provedor"""
        if provider_name in self.providers:
            self.providers[provider_name]['error_count'] += 1

            if self.providers[provider_name]['error_count'] >= self.providers[provider_name]['max_errors']:
                logger.warning(f"⚠️ Provedor {provider_name} desabilitado temporariamente")
                self.providers[provider_name]['enabled'] = False

    def get_provider_status(self) -> Dict[str, Any]:
        """Retorna status de todos os provedores"""
        status = {}

        for name, provider in self.providers.items():
            status[name] = {
                'enabled': provider['enabled'],
                'priority': provider['priority'],
                'error_count': provider['error_count'],
                'max_errors': provider['max_errors'],
                'available': provider['enabled'] and provider['error_count'] < provider['max_errors']
            }

        return status

# Instância global
unified_search_manager = UnifiedSearchManager()