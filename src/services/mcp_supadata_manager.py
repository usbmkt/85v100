
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ARQV30 Enhanced v2.0 - MCP SupaData Manager FUNCIONAL
Gerenciador de dados massivos com busca inteligente - FUNCIONANDO
"""

import os
import logging
import time
import json
from typing import Dict, List, Optional, Any
from datetime import datetime
from services.unified_search_manager import unified_search_manager
from services.robust_content_extractor import robust_content_extractor
from services.ai_manager import ai_manager

logger = logging.getLogger(__name__)

class MCPSupadataManager:
    """Gerenciador SupaData FUNCIONAL para coleta massiva de dados"""
    
    def __init__(self):
        """Inicializa SupaData Manager funcional"""
        self.enabled = True
        self.max_concurrent_searches = 5
        self.max_pages_per_search = 50
        self.data_quality_threshold = 0.7
        
        self.data_sources = {
            'web_search': {
                'enabled': True,
                'manager': unified_search_manager,
                'weight': 1.0
            },
            'content_extraction': {
                'enabled': True,
                'manager': robust_content_extractor,
                'weight': 0.8
            },
            'ai_analysis': {
                'enabled': True,
                'manager': ai_manager,
                'weight': 0.9
            }
        }
        
        logger.info("🚀 MCP SupaData Manager FUNCIONAL inicializado")
    
    def collect_massive_data(
        self, 
        query: str, 
        context: Dict[str, Any],
        depth_level: int = 3
    ) -> Dict[str, Any]:
        """Coleta dados massivos REAIS da web"""
        
        logger.info(f"📊 INICIANDO COLETA MASSIVA DE DADOS para: {query}")
        start_time = time.time()
        
        try:
            # 1. BUSCA MASSIVA NA WEB
            logger.info("🌐 Executando busca massiva na web...")
            web_data = self._execute_massive_web_search(query, context, depth_level)
            
            # 2. EXTRAÇÃO DE CONTEÚDO EM MASSA
            logger.info("📄 Executando extração massiva de conteúdo...")
            extracted_data = self._execute_massive_content_extraction(web_data)
            
            # 3. ANÁLISE INTELIGENTE DOS DADOS
            logger.info("🧠 Executando análise inteligente dos dados...")
            analyzed_data = self._execute_intelligent_analysis(extracted_data, query, context)
            
            # 4. CONSOLIDAÇÃO FINAL
            final_data = self._consolidate_massive_data(web_data, extracted_data, analyzed_data)
            
            collection_time = time.time() - start_time
            
            logger.info(f"✅ COLETA MASSIVA CONCLUÍDA em {collection_time:.2f}s")
            logger.info(f"📊 Dados coletados: {len(final_data.get('sources', []))} fontes")
            
            return final_data
            
        except Exception as e:
            logger.error(f"❌ Erro na coleta massiva: {str(e)}")
            return self._generate_emergency_data(query, context)
    
    def _execute_massive_web_search(
        self, 
        query: str, 
        context: Dict[str, Any],
        depth_level: int
    ) -> Dict[str, Any]:
        """Executa busca massiva na web"""
        
        try:
            # Gera queries relacionadas
            related_queries = self._generate_related_queries(query, context)
            all_search_results = []
            
            # Busca principal
            main_search = unified_search_manager.unified_search(
                query=query,
                max_results=30,
                context=context
            )
            all_search_results.extend(main_search.get('results', []))
            
            # Buscas relacionadas
            for related_query in related_queries[:depth_level]:
                try:
                    related_search = unified_search_manager.unified_search(
                        query=related_query,
                        max_results=20,
                        context=context
                    )
                    all_search_results.extend(related_search.get('results', []))
                    time.sleep(1)  # Rate limiting
                except Exception as e:
                    logger.warning(f"⚠️ Erro em query relacionada '{related_query}': {e}")
                    continue
            
            # Remove duplicatas
            unique_results = []
            seen_urls = set()
            
            for result in all_search_results:
                url = result.get('url', '')
                if url and url not in seen_urls:
                    seen_urls.add(url)
                    unique_results.append(result)
            
            return {
                'main_query': query,
                'related_queries': related_queries,
                'total_results': len(unique_results),
                'results': unique_results[:self.max_pages_per_search],
                'search_metadata': {
                    'timestamp': datetime.now().isoformat(),
                    'depth_level': depth_level
                }
            }
            
        except Exception as e:
            logger.error(f"❌ Erro na busca massiva: {e}")
            return {'results': [], 'error': str(e)}
    
    def _execute_massive_content_extraction(self, web_data: Dict[str, Any]) -> Dict[str, Any]:
        """Executa extração massiva de conteúdo"""
        
        try:
            results = web_data.get('results', [])
            extracted_contents = []
            successful_extractions = 0
            failed_extractions = 0
            
            for i, result in enumerate(results):
                url = result.get('url', '')
                
                try:
                    logger.info(f"📄 Extraindo conteúdo {i+1}/{len(results)}: {result.get('title', 'Sem título')}")
                    
                    content, metadata = robust_content_extractor.extract_content(url)
                    
                    if content and len(content) > 200:
                        extracted_contents.append({
                            'url': url,
                            'title': result.get('title', ''),
                            'content': content,
                            'extraction_time': time.time(),
                            'content_length': len(content),
                            'source': result.get('source', 'unknown')
                        })
                        successful_extractions += 1
                    else:
                        failed_extractions += 1
                        logger.warning(f"⚠️ Conteúdo insuficiente para: {url}")
                    
                    # Rate limiting
                    time.sleep(0.5)
                    
                except Exception as e:
                    failed_extractions += 1
                    logger.error(f"❌ Erro na extração de {url}: {e}")
                    continue
            
            return {
                'extracted_contents': extracted_contents,
                'statistics': {
                    'total_attempted': len(results),
                    'successful_extractions': successful_extractions,
                    'failed_extractions': failed_extractions,
                    'success_rate': (successful_extractions / len(results)) * 100 if results else 0
                },
                'metadata': {
                    'timestamp': datetime.now().isoformat(),
                    'total_content_chars': sum(len(c['content']) for c in extracted_contents)
                }
            }
            
        except Exception as e:
            logger.error(f"❌ Erro na extração massiva: {e}")
            return {'extracted_contents': [], 'error': str(e)}
    
    def _execute_intelligent_analysis(
        self, 
        extracted_data: Dict[str, Any], 
        query: str, 
        context: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Executa análise inteligente dos dados extraídos"""
        
        try:
            extracted_contents = extracted_data.get('extracted_contents', [])
            
            if not extracted_contents:
                return {'insights': [], 'error': 'Nenhum conteúdo para analisar'}
            
            # Combina conteúdos para análise
            combined_content = ""
            sources_info = []
            
            for content_item in extracted_contents[:10]:  # Top 10 conteúdos
                combined_content += f"\n--- FONTE: {content_item['title']} ---\n"
                combined_content += content_item['content'][:2000] + "\n"  # Limita cada fonte
                
                sources_info.append({
                    'title': content_item['title'],
                    'url': content_item['url'],
                    'content_length': content_item['content_length']
                })
            
            # Análise com IA
            analysis_prompt = f"""
            ANÁLISE INTELIGENTE DE DADOS MASSIVOS

            QUERY ORIGINAL: {query}
            
            CONTEXTO:
            - Segmento: {context.get('segmento', 'N/A')}
            - Produto: {context.get('produto', 'N/A')}
            - Público: {context.get('publico', 'N/A')}
            
            DADOS COLETADOS:
            {combined_content}
            
            TAREFA:
            Analise os dados coletados e extraia insights valiosos sobre:
            1. Tendências de mercado identificadas
            2. Oportunidades de negócio
            3. Dados estatísticos relevantes
            4. Insights sobre o público-alvo
            5. Informações sobre concorrência
            
            Forneça uma análise estruturada e detalhada.
            """
            
            ai_analysis = ai_manager.generate_content(
                prompt=analysis_prompt,
                max_tokens=3000,
                temperature=0.3
            )
            
            return {
                'ai_analysis': ai_analysis,
                'sources_analyzed': len(sources_info),
                'sources_info': sources_info,
                'combined_content_length': len(combined_content),
                'metadata': {
                    'timestamp': datetime.now().isoformat(),
                    'analysis_type': 'intelligent_massive_data'
                }
            }
            
        except Exception as e:
            logger.error(f"❌ Erro na análise inteligente: {e}")
            return {'ai_analysis': '', 'error': str(e)}
    
    def _consolidate_massive_data(
        self, 
        web_data: Dict[str, Any], 
        extracted_data: Dict[str, Any], 
        analyzed_data: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Consolida todos os dados coletados"""
        
        return {
            'supadata_collection': {
                'query': web_data.get('main_query', ''),
                'collection_timestamp': datetime.now().isoformat(),
                'data_quality_score': self._calculate_data_quality(web_data, extracted_data, analyzed_data),
                'collection_type': 'massive_web_scraping'
            },
            'web_search_data': {
                'total_results': web_data.get('total_results', 0),
                'related_queries': web_data.get('related_queries', []),
                'results': web_data.get('results', [])
            },
            'content_extraction_data': {
                'successful_extractions': extracted_data.get('statistics', {}).get('successful_extractions', 0),
                'success_rate': extracted_data.get('statistics', {}).get('success_rate', 0),
                'total_content_chars': extracted_data.get('metadata', {}).get('total_content_chars', 0),
                'extracted_contents': extracted_data.get('extracted_contents', [])
            },
            'intelligent_analysis': {
                'ai_analysis': analyzed_data.get('ai_analysis', ''),
                'sources_analyzed': analyzed_data.get('sources_analyzed', 0),
                'sources_info': analyzed_data.get('sources_info', [])
            },
            'statistics': {
                'total_sources': len(web_data.get('results', [])),
                'successfully_extracted': len(extracted_data.get('extracted_contents', [])),
                'data_sources_used': len([s for s in self.data_sources.values() if s['enabled']]),
                'collection_success': True
            }
        }
    
    def _generate_related_queries(self, query: str, context: Dict[str, Any]) -> List[str]:
        """Gera queries relacionadas para busca expandida"""
        
        segmento = context.get('segmento', '')
        produto = context.get('produto', '')
        publico = context.get('publico', '')
        
        related_queries = []
        
        # Queries baseadas no contexto
        if segmento:
            related_queries.append(f"{segmento} mercado brasileiro tendências 2024")
            related_queries.append(f"{segmento} oportunidades Brasil")
        
        if produto:
            related_queries.append(f"{produto} demanda mercado brasileiro")
            related_queries.append(f"{produto} concorrência análise Brasil")
        
        if publico:
            related_queries.append(f"{publico} comportamento consumo Brasil")
            related_queries.append(f"{publico} pesquisa mercado dados")
        
        # Queries genéricas de mercado
        related_queries.extend([
            f"{query} estatísticas Brasil 2024",
            f"{query} pesquisa mercado dados",
            f"{query} análise competitiva",
            f"{query} oportunidades investimento",
            f"{query} tendências futuro"
        ])
        
        return related_queries[:10]  # Máximo 10 queries relacionadas
    
    def _calculate_data_quality(
        self, 
        web_data: Dict[str, Any], 
        extracted_data: Dict[str, Any], 
        analyzed_data: Dict[str, Any]
    ) -> float:
        """Calcula score de qualidade dos dados coletados"""
        
        score = 0.0
        
        # Score baseado em quantidade de resultados
        total_results = web_data.get('total_results', 0)
        if total_results > 20:
            score += 0.3
        elif total_results > 10:
            score += 0.2
        elif total_results > 5:
            score += 0.1
        
        # Score baseado na taxa de extração
        success_rate = extracted_data.get('statistics', {}).get('success_rate', 0)
        score += (success_rate / 100) * 0.4
        
        # Score baseado na análise IA
        ai_analysis = analyzed_data.get('ai_analysis', '')
        if len(ai_analysis) > 1000:
            score += 0.3
        elif len(ai_analysis) > 500:
            score += 0.2
        elif len(ai_analysis) > 100:
            score += 0.1
        
        return min(score, 1.0)
    
    def _generate_emergency_data(self, query: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """Gera dados de emergência quando a coleta falha"""
        
        return {
            'supadata_collection': {
                'query': query,
                'collection_timestamp': datetime.now().isoformat(),
                'data_quality_score': 0.1,
                'collection_type': 'emergency_fallback',
                'error': 'Coleta massiva falhou - usando dados de emergência'
            },
            'web_search_data': {'total_results': 0, 'results': []},
            'content_extraction_data': {'successful_extractions': 0, 'extracted_contents': []},
            'intelligent_analysis': {
                'ai_analysis': f"Análise de emergência para '{query}'. Dados limitados disponíveis devido a falha na coleta massiva.",
                'sources_analyzed': 0
            },
            'statistics': {
                'total_sources': 0,
                'successfully_extracted': 0,
                'collection_success': False
            }
        }
    
    def is_available(self) -> bool:
        """Verifica se o SupaData Manager está disponível"""
        return self.enabled
    
    def get_status(self) -> Dict[str, Any]:
        """Retorna status do SupaData Manager"""
        return {
            'enabled': self.enabled,
            'data_sources': {name: source['enabled'] for name, source in self.data_sources.items()},
            'max_concurrent_searches': self.max_concurrent_searches,
            'max_pages_per_search': self.max_pages_per_search,
            'timestamp': datetime.now().isoformat()
        }

# Instância global
mcp_supadata_manager = MCPSupadataManager()
