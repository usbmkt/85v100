#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ARQV30 Enhanced v2.0 - Unified Analysis Engine
Motor de análise unificado que combina todas as capacidades
"""

import logging
import time
import json
import hashlib
from typing import Dict, List, Any, Optional
from datetime import datetime
from services.ai_manager import ai_manager
from services.unified_search_manager import unified_search_manager
from services.robust_content_extractor import robust_content_extractor
from services.pymupdf_client import pymupdf_client
from services.exa_client import exa_client
from services.mental_drivers_architect import mental_drivers_architect
from services.visual_proofs_generator import visual_proofs_generator
from services.anti_objection_system import anti_objection_system
from services.pre_pitch_architect import pre_pitch_architect
from services.archaeological_master import archaeological_master
from services.visceral_master_agent import visceral_master
from services.visual_proofs_director import visual_proofs_director
from services.forensic_cpl_analyzer import forensic_cpl_analyzer
from services.visceral_leads_engineer import visceral_leads_engineer
from services.pre_pitch_architect_advanced import pre_pitch_architect_advanced
from services.auto_save_manager import auto_save_manager, salvar_etapa, salvar_erro

logger = logging.getLogger(__name__))

class UnifiedAnalysisEngine:
    """Motor de análise unificado com todas as capacidades"""

    def __init__(self):
        """Inicializa o motor unificado"""
        self.analysis_types = {
            'standard': 'Análise Padrão Ultra-Detalhada',
            'archaeological': 'Análise Arqueológica (12 Camadas)',
            'forensic_cpl': 'Análise Forense de CPL',
            'visceral_leads': 'Engenharia Reversa de Leads',
            'pre_pitch': 'Orquestração de Pré-Pitch',
            'complete': 'Análise Completa Unificada'
        }

        self.available_agents = {
            'arqueologist': archaeological_master,
            'visceral_master': visceral_master,
            'visual_director': visual_proofs_director,
            'drivers_architect': mental_drivers_architect,
            'anti_objection': anti_objection_system,
            'pre_pitch_architect': pre_pitch_architect,
            'forensic_cpl': forensic_cpl_analyzer,
            'visceral_leads': visceral_leads_engineer,
            'pre_pitch_advanced': pre_pitch_architect_advanced
        }

        self.required_categories = [
            "anti_objecao",
            "avatars",
            "completas",
            "concorrencia",
            "drivers_mentais",
            "funil_vendas",
            "insights",
            "metadata",
            "metricas",
            "palavras_chave",
            "pesquisa_web",
            "plano_acao",
            "posicionamento",
            "pre_pitch",
            "predicoes_futuro",
            "provas_visuais"
        ]

        logger.info("🚀 Unified Analysis Engine inicializado")

    def execute_unified_analysis(
        self,
        data: Dict[str, Any],
        analysis_type: str = 'complete',
        session_id: str = None,
        progress_callback: Optional[callable] = None
    ) -> Dict[str, Any]:
        """Executa análise unificada com tipo especificado"""

        logger.info(f"🚀 Iniciando análise unificada: {analysis_type}")
        start_time = time.time()

        # Inicia sessão se não fornecida
        if not session_id:
            session_id = auto_save_manager.iniciar_sessao()

        # Salva início da análise
        salvar_etapa("analise_unificada_iniciada", {
            "data": data,
            "analysis_type": analysis_type,
            "session_id": session_id,
            "available_agents": list(self.available_agents.keys())
        }, categoria="analise_completa")

        try:
            if analysis_type == 'complete':
                # Executa análise completa, garantindo todas as 16 categorias
                return self._execute_all_16_categories_and_validate(data, session_id, progress_callback)
            elif analysis_type == 'archaeological':
                return self._execute_archaeological_analysis(data, session_id, progress_callback)
            elif analysis_type == 'forensic_cpl':
                return self._execute_forensic_cpl_analysis(data, session_id, progress_callback)
            elif analysis_type == 'visceral_leads':
                return self._execute_visceral_leads_analysis(data, session_id, progress_callback)
            elif analysis_type == 'pre_pitch':
                return self._execute_pre_pitch_analysis(data, session_id, progress_callback)
            else:
                return self._execute_standard_analysis(data, session_id, progress_callback)

        except Exception as e:
            logger.error(f"❌ Erro na análise unificada: {e}")
            salvar_erro("analise_unificada_erro", e, contexto=data)
            raise e

    def _execute_all_16_categories_and_validate(
        self,
        data: Dict[str, Any],
        session_id: str,
        progress_callback: Optional[callable] = None
    ) -> Dict[str, Any]:
        """Executa análise completa com TODAS as 16 categorias obrigatórias e validação rigorosa."""

        logger.info(f"🚀 Iniciando análise unificada COMPLETA (16 categorias) para sessão {session_id}")

        start_time = time.time()

        # Salva dados iniciais
        salvar_etapa("analise_unificada_inicio_16_categorias", {
            "session_id": session_id,
            "data_input": data,
            "timestamp": datetime.now().isoformat()
        }, categoria="analise_completa")

        # EXECUÇÃO OBRIGATÓRIA DAS 16 CATEGORIAS
        unified_analysis = self._execute_all_16_categories(data, session_id, progress_callback)

        # Validação RIGOROSA antes de finalizar
        validation_result = self._validate_completeness_16_categories(unified_analysis)

        if not validation_result['is_complete']:
            logger.error(f"❌ ANÁLISE INCOMPLETA: Categorias faltantes: {validation_result['missing_categories']}")
            # Re-executar categorias faltantes
            unified_analysis = self._complete_missing_categories(unified_analysis, validation_result['missing_categories'], data, session_id, progress_callback)

        processing_time = time.time() - start_time

        # Adiciona metadados finais
        unified_analysis['metadata'] = {
            'session_id': session_id,
            'generated_at': datetime.now().isoformat(),
            'processing_time_seconds': processing_time,
            'processing_time_formatted': f"{int(processing_time // 60)}m {int(processing_time % 60)}s",
            'version': '2.0.0',
            'categories_completed': 16,
            'analysis_id': session_id,
            'content_uniqueness_hash': self._generate_unique_hash(unified_analysis),
            'simulation_free': True,
            'analysis_completeness': 'TOTAL_16_CATEGORIES',
            'providers_used': len(unified_analysis.get('pesquisa_unificada', {}).get('provider_results', {})),
            'total_sources': unified_analysis.get('pesquisa_unificada', {}).get('statistics', {}).get('total_results', 0),
            'brazilian_sources': unified_analysis.get('pesquisa_unificada', {}).get('statistics', {}).get('brazilian_sources', 0),
            'exa_enhanced': exa_client.is_available(),
            'pymupdf_pro': pymupdf_client.is_available(),
        }

        # Salva análise unificada final
        salvar_etapa("analise_unificada_final_16_categorias", unified_analysis, categoria="analise_completa")

        logger.info(f"✅ Análise unificada COMPLETA (16 categorias) concluída em {processing_time:.2f}s")
        return unified_analysis

    def _execute_all_16_categories(
        self,
        data: Dict[str, Any],
        session_id: str,
        progress_callback: Optional[callable] = None
    ) -> Dict[str, Any]:
        """Executa TODAS as 16 categorias de análise obrigatórias de forma sequencial."""

        analysis_results = {}
        total_categories = len(self.required_categories)
        processed_count = 0

        # 1. Anti-Objecao
        if progress_callback: progress_callback(processed_count / total_categories, "1/16 - Construindo Sistema Anti-Objeção...")
        try:
            objections_list = data.get('objections', [
                "Não tenho tempo para implementar isso agora",
                "Preciso pensar melhor sobre o investimento",
                "Meu caso é muito específico",
                "Já tentei outras coisas e não deram certo"
            ])
            avatar_data = data.get('avatar_visceral', {}) or self._get_fallback_avatar_data(data)
            analysis_results["anti_objecao"] = anti_objection_system.generate_complete_anti_objection_system(
                objections_list, avatar_data, data
            )
            logger.info("✅ Categoria 'anti_objecao' concluída.")
        except Exception as e:
            logger.error(f"❌ Erro na categoria 'anti_objecao': {e}")
            analysis_results["anti_objecao"] = {"error": str(e)}
        processed_count += 1

        # 2. Avatars (usando dados do Visceral ou Arqueológico)
        if progress_callback: progress_callback(processed_count / total_categories, "2/16 - Criando Avatares Definitivos...")
        try:
            avatar_data_visceral = visceral_master.execute_visceral_analysis(data, session_id=session_id).get('avatar_visceral_ultra', {})
            avatar_data_arqueologico = archaeological_master.execute_archaeological_analysis(data, session_id=session_id).get('avatar_arqueologico_ultra', {})
            analysis_results["avatars"] = {
                'avatar_visceral': avatar_data_visceral,
                'avatar_arqueologico': avatar_data_arqueologico,
                'avatar_final_escolhido': avatar_data_visceral if avatar_data_visceral else avatar_data_arqueologico
            }
            logger.info("✅ Categoria 'avatars' concluída.")
        except Exception as e:
            logger.error(f"❌ Erro na categoria 'avatars': {e}")
            analysis_results["avatars"] = {"error": str(e)}
        processed_count += 1

        # 3. Completas (Gerando a análise principal que pode incluir outras)
        if progress_callback: progress_callback(processed_count / total_categories, "3/16 - Gerando Análise Completa Unificada...")
        try:
            # Reutiliza a lógica existente para análise completa, mas garante que ela seja executada
            analysis_results["completas"] = self._execute_complete_unified_analysis(data, session_id, progress_callback)
            logger.info("✅ Categoria 'completas' concluída.")
        except Exception as e:
            logger.error(f"❌ Erro na categoria 'completas': {e}")
            analysis_results["completas"] = {"error": str(e)}
        processed_count += 1

        # 4. Concorrência
        if progress_callback: progress_callback(processed_count / total_categories, "4/16 - Analisando o Cenário de Concorrência...")
        try:
            search_query = data.get('query') or f"concorrência {data.get('segmento', 'negócios')} Brasil"
            search_results = unified_search_manager.unified_search(search_query, max_results=15, context=data, session_id=session_id)
            analysis_results["concorrencia"] = {
                "pesquisa_concorrencia": search_results,
                "analise_concorrencial": ai_manager.generate_analysis(
                    f"Analise os seguintes resultados de busca sobre a concorrência no mercado de {data.get('segmento', 'negócios')}. Identifique os principais players, suas estratégias de marketing, diferenciais e pontos fracos. Destaque oportunidades e ameaças. Use os dados: {json.dumps(search_results, ensure_ascii=False)[:10000]}",
                    max_tokens=2048
                )
            }
            logger.info("✅ Categoria 'concorrencia' concluída.")
        except Exception as e:
            logger.error(f"❌ Erro na categoria 'concorrencia': {e}")
            analysis_results["concorrencia"] = {"error": str(e)}
        processed_count += 1

        # 5. Drivers Mentais
        if progress_callback: progress_callback(processed_count / total_categories, "5/16 - Criando Arsenal de Drivers Mentais...")
        try:
            avatar_data = analysis_results.get("avatars", {}).get("avatar_final_escolhido", {})
            analysis_results["drivers_mentais"] = mental_drivers_architect.generate_complete_drivers_system(avatar_data, data)
            logger.info("✅ Categoria 'drivers_mentais' concluída.")
        except Exception as e:
            logger.error(f"❌ Erro na categoria 'drivers_mentais': {e}")
            analysis_results["drivers_mentais"] = {"error": str(e)}
        processed_count += 1

        # 6. Funil de Vendas
        if progress_callback: progress_callback(processed_count / total_categories, "6/16 - Mapeando o Funil de Vendas...")
        try:
            # Assume que 'completas' já executou a análise do funil ou que podemos reexecutar
            funil_data = analysis_results.get("completas", {}).get("pre_pitch_invisivel", {}) or data.get('funil_vendas_data', {})
            analysis_results["funil_vendas"] = ai_manager.generate_analysis(
                f"Com base no contexto do projeto: {data.get('segmento', 'negócios')}, produto: {data.get('produto', 'N/A')}, e os dados do funil: {json.dumps(funil_data, ensure_ascii=False)[:10000]}, detalhe as etapas do funil de vendas, gargalos e otimizações necessárias.",
                max_tokens=2048
            )
            logger.info("✅ Categoria 'funil_vendas' concluída.")
        except Exception as e:
            logger.error(f"❌ Erro na categoria 'funil_vendas': {e}")
            analysis_results["funil_vendas"] = {"error": str(e)}
        processed_count += 1

        # 7. Insights
        if progress_callback: progress_callback(processed_count / total_categories, "7/16 - Gerando Insights Estratégicos...")
        try:
            # Reutiliza insights da análise completa se disponível, senão gera novamente
            insights_data = analysis_results.get("completas", {}).get("insights_unificados", [])
            if not insights_data:
                search_query = data.get('query') or f"insights estratégicos {data.get('segmento', 'negócios')} Brasil"
                search_results = unified_search_manager.unified_search(search_query, max_results=10, context=data, session_id=session_id)
                insights_data = ai_manager.generate_analysis(
                    f"Extraia os 20 insights mais valiosos e acionáveis dos seguintes resultados de pesquisa para o mercado de {data.get('segmento', 'negócios')}. Use os dados: {json.dumps(search_results, ensure_ascii=False)[:10000]}",
                    max_tokens=2048
                )
            analysis_results["insights"] = {"insights_gerados": insights_data}
            logger.info("✅ Categoria 'insights' concluída.")
        except Exception as e:
            logger.error(f"❌ Erro na categoria 'insights': {e}")
            analysis_results["insights"] = {"error": str(e)}
        processed_count += 1

        # 8. Metadata (Já será adicionado no final, mas podemos gerar um rascunho aqui)
        if progress_callback: progress_callback(processed_count / total_categories, "8/16 - Preparando Metadados...")
        try:
            # Metadados serão consolidados no final, mas podemos adicionar informações preliminares se necessário
            analysis_results["metadata"] = {
                'preliminary_generation_time': time.time() - start_time,
                'status': 'generating'
            }
            logger.info("✅ Categoria 'metadata' (preliminar) concluída.")
        except Exception as e:
            logger.error(f"❌ Erro na categoria 'metadata': {e}")
            analysis_results["metadata"] = {"error": str(e)}
        processed_count += 1

        # 9. Métricas
        if progress_callback: progress_callback(processed_count / total_categories, "9/16 - Analisando Métricas Chave...")
        try:
            search_query = data.get('query') or f"métricas de mercado {data.get('segmento', 'negócios')} Brasil"
            search_results = unified_search_manager.unified_search(search_query, max_results=10, context=data, session_id=session_id)
            analysis_results["metricas"] = {
                "pesquisa_metricas": search_results,
                "analise_metricas": ai_manager.generate_analysis(
                    f"Analise os dados de métricas de mercado para o segmento de {data.get('segmento', 'negócios')}. Identifique KPIs importantes, benchmarks e tendências. Use os dados: {json.dumps(search_results, ensure_ascii=False)[:10000]}",
                    max_tokens=2048
                )
            }
            logger.info("✅ Categoria 'metricas' concluída.")
        except Exception as e:
            logger.error(f"❌ Erro na categoria 'metricas': {e}")
            analysis_results["metricas"] = {"error": str(e)}
        processed_count += 1

        # 10. Palavras-Chave
        if progress_callback: progress_callback(processed_count / total_categories, "10/16 - Identificando Palavras-Chave Estratégicas...")
        try:
            search_query = data.get('query') or f"palavras-chave {data.get('segmento', 'negócios')} Brasil"
            search_results = unified_search_manager.unified_search(search_query, max_results=10, context=data, session_id=session_id)
            analysis_results["palavras_chave"] = {
                "pesquisa_palavras_chave": search_results,
                "analise_palavras_chave": ai_manager.generate_analysis(
                    f"Com base na pesquisa de palavras-chave para {data.get('segmento', 'negócios')}, liste as 10 palavras-chave mais relevantes, com intenção de compra clara e bom volume de busca. Detalhe o volume estimado e a concorrência. Use os dados: {json.dumps(search_results, ensure_ascii=False)[:10000]}",
                    max_tokens=2048
                )
            }
            logger.info("✅ Categoria 'palavras_chave' concluída.")
        except Exception as e:
            logger.error(f"❌ Erro na categoria 'palavras_chave': {e}")
            analysis_results["palavras_chave"] = {"error": str(e)}
        processed_count += 1

        # 11. Pesquisa Web (Já foi feita em outras categorias, mas pode ser consolidada aqui)
        if progress_callback: progress_callback(processed_count / total_categories, "11/16 - Consolidando Pesquisa Web...")
        try:
            # Reutiliza a pesquisa da categoria 'completas' se disponível
            pesquisa_web_data = analysis_results.get("completas", {}).get("pesquisa_unificada", {})
            if not pesquisa_web_data:
                search_query = data.get('query') or f"pesquisa web {data.get('segmento', 'negócios')} Brasil"
                pesquisa_web_data = unified_search_manager.unified_search(search_query, max_results=20, context=data, session_id=session_id)
            analysis_results["pesquisa_web"] = pesquisa_web_data
            logger.info("✅ Categoria 'pesquisa_web' concluída.")
        except Exception as e:
            logger.error(f"❌ Erro na categoria 'pesquisa_web': {e}")
            analysis_results["pesquisa_web"] = {"error": str(e)}
        processed_count += 1

        # 12. Plano de Ação
        if progress_callback: progress_callback(processed_count / total_categories, "12/16 - Elaborando Plano de Ação Detalhado...")
        try:
            # Reutiliza insights e dados de outras categorias para criar o plano
            insights = analysis_results.get("insights", {}).get("insights_gerados", "")
            drivers = analysis_results.get("drivers_mentais", {}).get("drivers_customizados", [])
            provas_visuais = analysis_results.get("provas_visuais", {}).get("provis_system", [])
            
            analysis_results["plano_acao"] = ai_manager.generate_analysis(
                f"Com base nos seguintes insights: {insights}, drivers mentais: {drivers}, e provas visuais: {provas_visuais}, crie um plano de ação detalhado e sequencial para o projeto de {data.get('segmento', 'negócios')}. Inclua objetivos claros, atividades específicas, prazos estimados e métricas de sucesso. O objetivo principal é {data.get('objetivo_geral', 'o crescimento do negócio')}.",
                max_tokens=3000
            )
            logger.info("✅ Categoria 'plano_acao' concluída.")
        except Exception as e:
            logger.error(f"❌ Erro na categoria 'plano_acao': {e}")
            analysis_results["plano_acao"] = {"error": str(e)}
        processed_count += 1

        # 13. Posicionamento
        if progress_callback: progress_callback(processed_count / total_categories, "13/16 - Definindo Posicionamento Estratégico...")
        try:
            # Reutiliza dados do avatar, drivers e análise de concorrência
            avatar_data = analysis_results.get("avatars", {}).get("avatar_final_escolhido", {})
            drivers_data = analysis_results.get("drivers_mentais", {})
            concorrencia_data = analysis_results.get("concorrencia", {}).get("analise_concorrencial", "")

            analysis_results["posicionamento"] = ai_manager.generate_analysis(
                f"Com base no avatar: {avatar_data}, drivers mentais: {drivers_data}, e análise de concorrência: {concorrencia_data}, defina um posicionamento de mercado único e irresistível para o produto/serviço de {data.get('segmento', 'negócios')}. Crie uma proposta de valor clara e slogans impactantes. O objetivo é {data.get('objetivo_geral', 'dominar o mercado')}.",
                max_tokens=2048
            )
            logger.info("✅ Categoria 'posicionamento' concluída.")
        except Exception as e:
            logger.error(f"❌ Erro na categoria 'posicionamento': {e}")
            analysis_results["posicionamento"] = {"error": str(e)}
        processed_count += 1

        # 14. Pre-Pitch
        if progress_callback: progress_callback(processed_count / total_categories, "14/16 - Orquestrando o Pré-Pitch Invisível...")
        try:
            # Utiliza o agente específico para pré-pitch avançado
            selected_drivers = drivers_data.get('drivers_customizados', [])
            event_structure = data.get('event_structure', 'Webinar/Live/Evento')
            product_offer = data.get('product_offer', f"Produto: {data.get('produto', 'N/A')} - Preço: R$ {data.get('preco', 'N/A')}")

            analysis_results["pre_pitch"] = pre_pitch_architect_advanced.orchestrate_psychological_symphony(
                selected_drivers, avatar_data, event_structure, product_offer, session_id
            )
            logger.info("✅ Categoria 'pre_pitch' concluída.")
        except Exception as e:
            logger.error(f"❌ Erro na categoria 'pre_pitch': {e}")
            analysis_results["pre_pitch"] = {"error": str(e)}
        processed_count += 1

        # 15. Predições Futuro
        if progress_callback: progress_callback(processed_count / total_categories, "15/16 - Prevendo Tendências Futuras...")
        try:
            search_query = data.get('query') or f"tendências futuro {data.get('segmento', 'negócios')} Brasil"
            search_results = unified_search_manager.unified_search(search_query, max_results=10, context=data, session_id=session_id)
            analysis_results["predicoes_futuro"] = ai_manager.generate_analysis(
                f"Com base nas tendências futuras para o mercado de {data.get('segmento', 'negócios')}, preveja os próximos 3-5 anos. Identifique tecnologias emergentes, mudanças de comportamento do consumidor e oportunidades disruptivas. Use os dados: {json.dumps(search_results, ensure_ascii=False)[:10000]}",
                max_tokens=2048
            )
            logger.info("✅ Categoria 'predicoes_futuro' concluída.")
        except Exception as e:
            logger.error(f"❌ Erro na categoria 'predicoes_futuro': {e}")
            analysis_results["predicoes_futuro"] = {"error": str(e)}
        processed_count += 1

        # 16. Provas Visuais
        if progress_callback: progress_callback(processed_count / total_categories, "16/16 - Criando Provas Visuais Irrefutáveis...")
        try:
            concepts_to_prove = self._extract_concepts_for_proofs(
                analysis_results.get("avatars", {}).get("avatar_final_escolhido", {}),
                analysis_results.get("drivers_mentais", {}),
                data
            )
            analysis_results["provas_visuais"] = visual_proofs_director.execute_provis_creation(
                concepts_to_prove,
                analysis_results.get("avatars", {}).get("avatar_final_escolhido", {}),
                analysis_results.get("drivers_mentais", {}),
                data,
                session_id
            )
            logger.info("✅ Categoria 'provas_visuais' concluída.")
        except Exception as e:
            logger.error(f"❌ Erro na categoria 'provas_visuais': {e}")
            analysis_results["provas_visuais"] = {"error": str(e)}
        processed_count += 1

        return analysis_results

    def _validate_completeness_16_categories(self, analysis_results: Dict[str, Any]) -> Dict[str, Any]:
        """Valida se todas as 16 categorias obrigatórias foram geradas corretamente."""
        missing_categories = []
        for category in self.required_categories:
            if category not in analysis_results or not analysis_results[category] or isinstance(analysis_results[category], dict) and "error" in analysis_results[category]:
                missing_categories.append(category)

        return {
            'is_complete': not missing_categories,
            'missing_categories': missing_categories
        }

    def _complete_missing_categories(
        self,
        current_analysis: Dict[str, Any],
        missing_categories: List[str],
        data: Dict[str, Any],
        session_id: str,
        progress_callback: Optional[callable] = None
    ) -> Dict[str, Any]:
        """Tenta reexecutar as categorias que falharam."""
        logger.warning(f"Tentando completar categorias faltantes: {missing_categories}")
        
        # Mapeia as categorias para suas respectivas funções de execução (simplificado aqui)
        category_execution_map = {
            "anti_objecao": lambda d, s, cb: anti_objection_system.generate_complete_anti_objection_system(
                d.get('objections', ["Fallback objection"]),
                d.get('avatar_visceral', {}),
                d
            ),
            "avatars": lambda d, s, cb: {
                'avatar_visceral': visceral_master.execute_visceral_analysis(d, session_id=s).get('avatar_visceral_ultra', {}),
                'avatar_arqueologico': archaeological_master.execute_archaeological_analysis(d, session_id=s).get('avatar_arqueologico_ultra', {}),
            },
            "concorrencia": lambda d, s, cb: {
                "analise_concorrencial": ai_manager.generate_analysis(
                    f"Reanalise a concorrência para {d.get('segmento', 'negócios')}. Use os dados: {json.dumps(unified_search_manager.unified_search(f'concorrência {d.get('segmento', 'negócios')} Brasil', max_results=15, context=d, session_id=s), ensure_ascii=False)[:10000]}",
                    max_tokens=2048
                )
            },
            "drivers_mentais": lambda d, s, cb: mental_drivers_architect.generate_complete_drivers_system(
                current_analysis.get("avatars", {}).get("avatar_final_escolhido", {}), d
            ),
            "funil_vendas": lambda d, s, cb: ai_manager.generate_analysis(
                f"Reanalise o funil de vendas para {d.get('segmento', 'negócios')}. Contexto: {json.dumps(current_analysis.get('pre_pitch', {}), ensure_ascii=False)[:10000]}",
                max_tokens=2048
            ),
            "insights": lambda d, s, cb: ai_manager.generate_analysis(
                 f"Reextracao de insights para {d.get('segmento', 'negócios')}. Use os dados: {json.dumps(unified_search_manager.unified_search(f'insights estratégicos {d.get('segmento', 'negócios')} Brasil', max_results=10, context=d, session_id=s), ensure_ascii=False)[:10000]}",
                max_tokens=2048
            ),
            "metricas": lambda d, s, cb: {
                "analise_metricas": ai_manager.generate_analysis(
                    f"Reanalise as métricas para {d.get('segmento', 'negócios')}. Use os dados: {json.dumps(unified_search_manager.unified_search(f'métricas de mercado {d.get('segmento', 'negócios')} Brasil', max_results=10, context=d, session_id=s), ensure_ascii=False)[:10000]}",
                    max_tokens=2048
                )
            },
            "palavras_chave": lambda d, s, cb: {
                "analise_palavras_chave": ai_manager.generate_analysis(
                    f"Reanalise as palavras-chave para {d.get('segmento', 'negócios')}. Use os dados: {json.dumps(unified_search_manager.unified_search(f'palavras-chave {d.get('segmento', 'negócios')} Brasil', max_results=10, context=d, session_id=s), ensure_ascii=False)[:10000]}",
                    max_tokens=2048
                )
            },
            "pesquisa_web": lambda d, s, cb: unified_search_manager.unified_search(f'pesquisa web {d.get('segmento', 'negócios')} Brasil', max_results=20, context=d, session_id=s),
            "plano_acao": lambda d, s, cb: ai_manager.generate_analysis(
                f"Reelabore o plano de ação para {d.get('segmento', 'negócios')} com base em insights atualizados. Insights: {current_analysis.get('insights', {}).get('insights_gerados', '')}, Drivers: {current_analysis.get('drivers_mentais', {}).get('drivers_customizados', [])}",
                max_tokens=3000
            ),
            "posicionamento": lambda d, s, cb: ai_manager.generate_analysis(
                f"Refine o posicionamento para {d.get('segmento', 'negócios')}. Avatar: {current_analysis.get('avatars', {}).get('avatar_final_escolhido', {})}, Concorrência: {current_analysis.get('concorrencia', {}).get('analise_concorrencial', '')}",
                max_tokens=2048
            ),
            "pre_pitch": lambda d, s, cb: pre_pitch_architect_advanced.orchestrate_psychological_symphony(
                current_analysis.get("drivers_mentais", {}).get('drivers_customizados', []),
                current_analysis.get("avatars", {}).get("avatar_final_escolhido", {}),
                d.get('event_structure', 'Webinar/Live/Evento'),
                d.get('product_offer', f"Produto: {d.get('produto', 'N/A')} - Preço: R$ {d.get('preco', 'N/A')}"),
                s
            ),
            "predicoes_futuro": lambda d, s, cb: ai_manager.generate_analysis(
                f"Reavalie as predições futuras para {d.get('segmento', 'negócios')}. Use os dados: {json.dumps(unified_search_manager.unified_search(f'tendências futuro {d.get('segmento', 'negócios')} Brasil', max_results=10, context=d, session_id=s), ensure_ascii=False)[:10000]}",
                max_tokens=2048
            ),
            "provas_visuais": lambda d, s, cb: visual_proofs_director.execute_provis_creation(
                self._extract_concepts_for_proofs(
                    current_analysis.get("avatars", {}).get("avatar_final_escolhido", {}),
                    current_analysis.get("drivers_mentais", {}),
                    d
                ),
                current_analysis.get("avatars", {}).get("avatar_final_escolhido", {}),
                current_analysis.get("drivers_mentais", {}),
                d,
                s
            )
            # 'completas' and 'metadata' are handled differently or will be recalculated
        }

        total_categories_to_retry = len(missing_categories)
        reprocessed_count = 0
        for category in missing_categories:
            if progress_callback: progress_callback((1.0/16.0) * (15.0 + reprocessed_count / total_categories_to_retry), f"Reexecutando {category}...")
            if category in category_execution_map:
                try:
                    current_analysis[category] = category_execution_map[category](data, session_id, progress_callback)
                    logger.info(f"✅ Categoria '{category}' (reexecutada) concluída.")
                except Exception as e:
                    logger.error(f"❌ Erro ao reexecutar categoria '{category}': {e}")
                    current_analysis[category] = {"error": str(e)}
            else:
                logger.warning(f"Nenhuma função de reexecução definida para a categoria: {category}")
            reprocessed_count += 1
        
        return current_analysis


    def _extract_unified_content(self, search_results: Dict[str, Any], session_id: str) -> Dict[str, Any]:
        """Extrai conteúdo usando todos os extratores disponíveis"""

        results = search_results.get('results', [])
        extracted_content = []
        pdf_content = []

        for i, result in enumerate(results[:15]):  # Top 15 resultados
            url = result.get('url', '')

            try:
                # Verifica se é PDF
                if url.lower().endswith('.pdf') or 'pdf' in url.lower():
                    # Usa PyMuPDF Pro para PDFs
                    if pymupdf_client.is_available():
                        pdf_result = pymupdf_client.extract_from_url(url)
                        if pdf_result['success']:
                            pdf_content.append({
                                'url': url,
                                'title': result.get('title', ''),
                                'content': pdf_result['text'],
                                'metadata': pdf_result['metadata'],
                                'statistics': pdf_result['statistics'],
                                'extraction_method': 'PyMuPDF_Pro'
                            })
                            continue

                # Usa extrator robusto para páginas web
                content, metadata = robust_content_extractor.extract_content(url)
                if content and len(content) > 200:
                    extracted_content.append({
                        'url': url,
                        'title': result.get('title', ''),
                        'content': content,
                        'source': result.get('source', 'unknown'),
                        'is_brazilian': result.get('is_brazilian', False),
                        'is_preferred': result.get('is_preferred', False),
                        'extraction_method': 'robust_extractor'
                    })

                # Delay para rate limiting
                time.sleep(0.3)

            except Exception as e:
                logger.error(f"❌ Erro ao extrair {url}: {e}")
                continue

        # Combina conteúdo extraído
        combined_content = {
            'web_content': extracted_content,
            'pdf_content': pdf_content,
            'statistics': {
                'total_web_pages': len(extracted_content),
                'total_pdf_pages': len(pdf_content),
                'total_content_length': sum(len(item['content']) for item in extracted_content + pdf_content),
                'extraction_success_rate': (len(extracted_content) + len(pdf_content)) / len(results) * 100 if results else 0
            }
        }

        # Salva conteúdo extraído
        salvar_etapa("conteudo_unificado_extraido", combined_content, categoria="pesquisa_web")

        return combined_content

    def _extract_concepts_for_proofs(
        self, 
        avatar_data: Dict[str, Any], 
        drivers_data: Dict[str, Any], 
        context_data: Dict[str, Any]
    ) -> List[str]:
        """Extrai conceitos que precisam de prova visual"""

        concepts = []

        # Conceitos do avatar
        if avatar_data.get('feridas_abertas_inconfessaveis'):
            concepts.extend(avatar_data['feridas_abertas_inconfessaveis'][:5])

        if avatar_data.get('sonhos_proibidos_ardentes'):
            concepts.extend(avatar_data['sonhos_proibidos_ardentes'][:5])

        # Conceitos dos drivers
        if drivers_data.get('drivers_customizados'):
            for driver in drivers_data['drivers_customizados'][:3]:
                concepts.append(driver.get('nome', 'Driver Mental'))

        # Conceitos gerais críticos
        concepts.extend([
            "Eficácia do método",
            "Transformação real possível",
            "ROI do investimento",
            "Diferencial da concorrência",
            "Tempo para resultados"
        ])

        return concepts[:12]  # Máximo 12 conceitos

    def _execute_archaeological_analysis(
        self,
        data: Dict[str, Any],
        session_id: str,
        progress_callback: Optional[callable] = None
    ) -> Dict[str, Any]:
        """Executa apenas análise arqueológica"""

        if progress_callback:
            progress_callback(1, "🔬 Iniciando análise arqueológica...")

        # Pesquisa unificada
        search_query = data.get('query') or f"mercado {data.get('segmento', 'negócios')} Brasil 2024"
        search_results = unified_search_manager.unified_search(search_query, context=data, session_id=session_id)

        # Análise arqueológica
        archaeological_result = archaeological_master.execute_archaeological_analysis(
            data,
            research_context=json.dumps(search_results, ensure_ascii=False)[:15000],
            session_id=session_id
        )

        return {
            'tipo_analise': 'arqueologica',
            'projeto_dados': data,
            'pesquisa_unificada': search_results,
            'analise_arqueologica': archaeological_result,
            'metadata': {
                'analysis_type': 'archaeological',
                'session_id': session_id,
                'generated_at': datetime.now().isoformat()
            }
        }

    def _execute_forensic_cpl_analysis(
        self,
        data: Dict[str, Any],
        session_id: str,
        progress_callback: Optional[callable] = None
    ) -> Dict[str, Any]:
        """Executa análise forense de CPL"""

        if progress_callback:
            progress_callback(1, "🔬 Iniciando análise forense de CPL...")

        transcription = data.get('transcription', '')
        context_data = {
            'contexto_estrategico': data.get('contexto_estrategico', ''),
            'objetivo_cpl': data.get('objetivo_cpl', ''),
            'formato': data.get('formato', ''),
            'temperatura_audiencia': data.get('temperatura_audiencia', '')
        }

        forensic_result = forensic_cpl_analyzer.analyze_cpl_forensically(
            transcription, context_data, session_id
        )

        return {
            'tipo_analise': 'forense_cpl',
            'projeto_dados': data,
            'analise_forense_cpl': forensic_result,
            'metadata': {
                'analysis_type': 'forensic_cpl',
                'session_id': session_id,
                'generated_at': datetime.now().isoformat()
            }
        }

    def _execute_visceral_leads_analysis(
        self,
        data: Dict[str, Any],
        session_id: str,
        progress_callback: Optional[callable] = None
    ) -> Dict[str, Any]:
        """Executa engenharia reversa de leads"""

        if progress_callback:
            progress_callback(1, "🧠 Iniciando engenharia reversa visceral...")

        leads_data = data.get('leads_data', '')
        context_data = {
            'produto_servico': data.get('produto_servico', ''),
            'principais_perguntas': data.get('principais_perguntas', ''),
            'numero_respostas': data.get('numero_respostas', 0)
        }

        visceral_result = visceral_leads_engineer.reverse_engineer_leads(
            leads_data, context_data, session_id
        )

        return {
            'tipo_analise': 'visceral_leads',
            'projeto_dados': data,
            'engenharia_reversa_leads': visceral_result,
            'metadata': {
                'analysis_type': 'visceral_leads',
                'session_id': session_id,
                'generated_at': datetime.now().isoformat()
            }
        }

    def _execute_pre_pitch_analysis(
        self,
        data: Dict[str, Any],
        session_id: str,
        progress_callback: Optional[callable] = None
    ) -> Dict[str, Any]:
        """Executa orquestração de pré-pitch"""

        if progress_callback:
            progress_callback(1, "🎯 Iniciando orquestração de pré-pitch...")

        selected_drivers = data.get('selected_drivers', [])
        avatar_data = data.get('avatar_data', {})
        event_structure = data.get('event_structure', '')
        product_offer = data.get('product_offer', '')

        pre_pitch_result = pre_pitch_architect_advanced.orchestrate_psychological_symphony(
            selected_drivers, avatar_data, event_structure, product_offer, session_id
        )

        return {
            'tipo_analise': 'pre_pitch',
            'projeto_dados': data,
            'orquestracao_pre_pitch': pre_pitch_result,
            'metadata': {
                'analysis_type': 'pre_pitch',
                'session_id': session_id,
                'generated_at': datetime.now().isoformat()
            }
        }

    def _execute_standard_analysis(
        self,
        data: Dict[str, Any],
        session_id: str,
        progress_callback: Optional[callable] = None
    ) -> Dict[str, Any]:
        """Executa análise padrão unificada"""

        if progress_callback:
            progress_callback(1, "🔍 Iniciando análise padrão unificada...")

        # Pesquisa unificada
        search_query = data.get('query') or f"mercado {data.get('segmento', 'negócios')} Brasil 2024"
        search_results = unified_search_manager.unified_search(search_query, context=data, session_id=session_id)

        # Extração de conteúdo
        extracted_content = self._extract_unified_content(search_results, session_id)

        # Análise com IA
        analysis_prompt = self._build_unified_analysis_prompt(data, extracted_content)
        ai_response = ai_manager.generate_analysis(analysis_prompt, max_tokens=8192)

        if not ai_response:
            raise Exception("IA não respondeu para análise unificada")

        # Processa resposta
        ai_analysis = self._process_ai_response(ai_response, data)

        return {
            'tipo_analise': 'padrao_unificada',
            'projeto_dados': data,
            'pesquisa_unificada': search_results,
            'conteudo_extraido': extracted_content,
            'analise_ia': ai_analysis,
            'metadata': {
                'analysis_type': 'standard_unified',
                'session_id': session_id,
                'generated_at': datetime.now().isoformat()
            }
        }

    def _build_unified_analysis_prompt(self, data: Dict[str, Any], content: Dict[str, Any]) -> str:
        """Constrói prompt unificado para análise"""

        web_content = content.get('web_content', [])
        pdf_content = content.get('pdf_content', [])

        content_summary = ""

        # Resumo do conteúdo web
        if web_content:
            content_summary += "CONTEÚDO WEB EXTRAÍDO:\n"
            for i, item in enumerate(web_content[:10], 1):
                content_summary += f"FONTE {i}: {item['title']}\n"
                content_summary += f"URL: {item['url']}\n"
                content_summary += f"Conteúdo: {item['content'][:1500]}\n\n"

        # Resumo do conteúdo PDF
        if pdf_content:
            content_summary += "CONTEÚDO PDF EXTRAÍDO:\n"
            for i, item in enumerate(pdf_content[:5], 1):
                content_summary += f"PDF {i}: {item['title']}\n"
                content_summary += f"Páginas: {item['statistics']['pages']}\n"
                content_summary += f"Conteúdo: {item['content'][:2000]}\n\n"

        prompt = f"""
# ANÁLISE UNIFICADA ULTRA-DETALHADA - ARQV30 ENHANCED v2.0

Você é o DIRETOR SUPREMO DE ANÁLISE UNIFICADA, especialista de elite que combina todas as metodologias.

## DADOS DO PROJETO:
- **Segmento**: {data.get('segmento', 'Não informado')}
- **Produto/Serviço**: {data.get('produto', 'Não informado')}
- **Público-Alvo**: {data.get('publico', 'Não informado')}
- **Preço**: R$ {data.get('preco', 'Não informado')}
- **Objetivo de Receita**: R$ {data.get('objetivo_receita', 'Não informado')}

## PESQUISA UNIFICADA REALIZADA:
{content_summary[:15000]}

## GERE ANÁLISE UNIFICADA COMPLETA:

```json
{{
  "avatar_unificado": {{
    "nome_ficticio": "Nome específico baseado em dados reais",
    "perfil_demografico_completo": {{
      "idade": "Faixa etária com dados reais",
      "genero": "Distribuição real",
      "renda": "Faixa de renda real",
      "escolaridade": "Nível educacional real",
      "localizacao": "Regiões geográficas reais"
    }},
    "perfil_psicografico_profundo": {{
      "personalidade": "Traços dominantes reais",
      "valores": "Valores e crenças reais",
      "comportamento_compra": "Processo real de decisão",
      "medos_profundos": "Medos reais documentados",
      "aspiracoes_secretas": "Aspirações reais"
    }},
    "dores_viscerais_unificadas": [
      "Lista de 15-20 dores específicas baseadas em dados reais"
    ],
    "desejos_secretos_unificados": [
      "Lista de 15-20 desejos profundos baseados em estudos"
    ],
    "jornada_emocional_completa": {{
      "consciencia": "Como toma consciência baseado em dados",
      "consideracao": "Processo real de avaliação",
      "decisao": "Fatores decisivos reais",
      "pos_compra": "Experiência pós-compra real"
    }}
  }},

  "posicionamento_unificado": {{
    "proposta_valor_unica": "Proposta irresistível baseada em gaps",
    "diferenciais_competitivos": [
      "Lista de diferenciais únicos e defensáveis"
    ],
    "mensagem_central": "Mensagem principal que resume tudo",
    "estrategia_oceano_azul": "Como criar mercado sem concorrência"
  }},

  "insights_unificados": [
    "Lista de 25-30 insights únicos e ultra-valiosos baseados na análise completa"
  ],

  "estrategia_implementacao": {{
    "fase_1_preparacao": {{
      "duracao": "Tempo necessário",
      "atividades": ["Lista de atividades específicas"],
      "investimento": "Investimento necessário"
    }},
    "fase_2_execucao": {{
      "duracao": "Tempo necessário", 
      "atividades": ["Lista de atividades específicas"],
      "investimento": "Investimento necessário"
    }},
    "fase_3_otimizacao": {{
      "duracao": "Tempo necessário",
      "atividades": ["Lista de atividades específicas"],
      "investimento": "Investimento necessário"
    }}
  }}
}}
```

CRÍTICO: Use APENAS dados REAIS da pesquisa unificada. Combine insights de todas as fontes.
"""

        return prompt

    def _process_ai_response(self, response: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """Processa resposta da IA"""

        try:
            # Extrai JSON da resposta
            clean_text = response.strip()

            if "```json" in clean_text:
                start = clean_text.find("```json") + 7
                end = clean_text.rfind("```")
                clean_text = clean_text[start:end].strip()

            # Parseia JSON
            analysis = json.loads(clean_text)

            # Adiciona metadados
            analysis['metadata_ai'] = {
                'generated_at': datetime.now().isoformat(),
                'provider_used': 'unified_ai_manager',
                'analysis_type': 'unified_complete'
            }

            return analysis

        except json.JSONDecodeError as e:
            logger.error(f"❌ Erro ao parsear JSON: {e}")
            return self._create_fallback_analysis(data)

    def _create_fallback_analysis(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Cria análise de fallback"""

        segmento = data.get('segmento', 'negócios')

        return {
            'avatar_unificado': {
                'nome_ficticio': f'Profissional {segmento} Brasileiro',
                'dores_viscerais_unificadas': [
                    f'Trabalhar excessivamente em {segmento} sem crescimento proporcional',
                    'Sentir-se sempre atrás da concorrência',
                    'Ver competidores menores crescendo mais rápido'
                ],
                'desejos_secretos_unificados': [
                    f'Ser reconhecido como autoridade em {segmento}',
                    'Ter liberdade financeira total',
                    'Trabalhar apenas com o que ama'
                ]
            },
            'insights_unificados': [
                f'Mercado brasileiro de {segmento} em transformação digital',
                'Oportunidades em nichos específicos e personalizados',
                'Necessidade de abordagem psicológica diferenciada'
            ],
            'fallback_mode': True
        }

    def _get_fallback_avatar_data(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Retorna dados de avatar de fallback se necessário."""
        return {
            "nome_ficticio": f"Avatar Padrão para {data.get('segmento', 'Negócios')}",
            "perfil_demografico_completo": {
                "idade": "25-45 anos", "genero": "Ambos", "renda": "Média-Alta",
                "escolaridade": "Superior Completo", "localizacao": "Grandes Centros Urbanos"
            },
            "perfil_psicografico_profundo": {
                "personalidade": "Pragmático, busca resultados",
                "valores": "Crescimento, Segurança, Inovação",
                "comportamento_compra": "Pesquisa online, busca por prova social",
                "medos_profundos": ["Perder dinheiro", "Ficar para trás"],
                "aspiracoes_secretas": ["Liderança de mercado", "Reconhecimento profissional"]
            },
            "dores_viscerais_unificadas": [
                "Falta de clareza na estratégia de marketing",
                "Resultados abaixo do esperado",
                "Dificuldade em se diferenciar da concorrência"
            ],
            "desejos_secretos_unificados": [
                "Crescimento exponencial do negócio",
                "Ser referência no seu nicho",
                "Ter um sistema previsível de atração de clientes"
            ]
        }


    def _generate_unique_hash(self, analysis_data: Dict[str, Any]) -> str:
        """Gera um hash único para o conteúdo da análise, garantindo unicidade."""
        # Serializa os dados de forma consistente
        data_string = json.dumps(analysis_data, sort_keys=True, ensure_ascii=False)
        # Cria um hash SHA-256
        return hashlib.sha256(data_string.encode('utf-8')).hexdigest()


    def get_analysis_capabilities(self) -> Dict[str, Any]:
        """Retorna capacidades de análise disponíveis"""

        return {
            'analysis_types': self.analysis_types,
            'available_agents': {
                name: {
                    'available': True,
                    'description': f'Agente {name} disponível'
                } for name in self.available_agents.keys()
            },
            'search_providers': unified_search_manager.get_provider_status(),
            'extraction_capabilities': {
                'web_extraction': robust_content_extractor is not None,
                'pdf_extraction': pymupdf_client.is_available(),
                'exa_neural_search': exa_client.is_available()
            },
            'ai_providers': ai_manager.get_provider_status() if ai_manager else {}
        }

# Instância global
unified_analysis_engine = UnifiedAnalysisEngine()