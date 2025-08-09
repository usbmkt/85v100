#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ARQV30 Enhanced v2.0 - Enhanced Analysis Route CORRIGIDA
Rota principal para análise aprimorada - FUNCIONANDO
"""

from flask import Blueprint, request, jsonify
import logging
import time
import uuid
from datetime import datetime
from services.auto_save_manager import salvar_etapa, salvar_erro
from services.unified_search_manager import unified_search_manager
from services.robust_content_extractor import robust_content_extractor
from services.mcp_supadata_manager import mcp_supadata_manager
from services.ai_manager import ai_manager

logger = logging.getLogger(__name__)

enhanced_analysis_bp = Blueprint('enhanced_analysis', __name__)

@enhanced_analysis_bp.route('/analyze_ultra_enhanced', methods=['POST'])
def analyze_ultra_enhanced():
    """Endpoint principal para análise ultra aprimorada CORRIGIDA"""

    session_id = f"enhanced_{int(time.time() * 1000)}_{uuid.uuid4().hex[:8]}"

    try:
        # Recebe dados do formulário
        form_data = request.get_json() if request.is_json else request.form.to_dict()

        logger.info(f"🚀 INICIANDO ANÁLISE REAL: {session_id}")
        salvar_etapa('analise_iniciada', {
            'session_id': session_id,
            'form_data': form_data,
            'timestamp': datetime.now().isoformat()
        }, categoria="analise_completa")

        # Extrai informações do formulário
        segmento = form_data.get('segmento', '')
        produto = form_data.get('produto', '')
        publico = form_data.get('publico', '')

        if not all([segmento, produto, publico]):
            return jsonify({
                'success': False,
                'error': 'Campos obrigatórios não preenchidos',
                'session_id': session_id
            }), 400

        # Constrói contexto da análise
        context = {
            'segmento': segmento,
            'produto': produto,
            'publico': publico,
            'preco': form_data.get('preco'),
            'objetivo_receita': form_data.get('objetivo_receita'),
            'orcamento_marketing': form_data.get('orcamento_marketing'),
            'prazo_lancamento': form_data.get('prazo_lancamento'),
            'concorrentes': form_data.get('concorrentes'),
            'dados_adicionais': form_data.get('dados_adicionais')
        }

        # Query principal para busca
        main_query = f"{segmento} {produto} {publico} mercado brasileiro"

        logger.info(f"📊 Iniciando análise para: {main_query}")

        # 1. COLETA MASSIVA DE DADOS
        logger.info("🌐 EXECUTANDO COLETA MASSIVA DE DADOS...")
        supadata_result = mcp_supadata_manager.collect_massive_data(
            query=main_query,
            context=context,
            depth_level=3
        )

        salvar_etapa('supadata_coletado', supadata_result, categoria="analise_completa")

        # 2. ANÁLISE ESPECÍFICA DO MERCADO
        logger.info("📈 EXECUTANDO ANÁLISE ESPECÍFICA DO MERCADO...")
        market_search = unified_search_manager.unified_search(
            query=f"{segmento} análise mercado brasileiro tendências 2024",
            max_results=15,
            context=context,
            session_id=session_id
        )

        salvar_etapa('busca_mercado', market_search, categoria="analise_completa")

        # 3. ANÁLISE DO PÚBLICO-ALVO
        logger.info("👥 EXECUTANDO ANÁLISE DO PÚBLICO-ALVO...")
        audience_search = unified_search_manager.unified_search(
            query=f"{publico} comportamento consumo {segmento} Brasil",
            max_results=10,
            context=context,
            session_id=session_id
        )

        salvar_etapa('busca_publico', audience_search, categoria="analise_completa")

        # 4. ANÁLISE DA CONCORRÊNCIA
        logger.info("⚔️ EXECUTANDO ANÁLISE DA CONCORRÊNCIA...")
        competition_query = f"{produto} concorrentes {segmento} Brasil"
        if context.get('concorrentes'):
            competition_query += f" {context['concorrentes']}"

        competition_search = unified_search_manager.unified_search(
            query=competition_query,
            max_results=12,
            context=context,
            session_id=session_id
        )

        salvar_etapa('busca_concorrencia', competition_search, categoria="analise_completa")

        # 5. EXTRAÇÃO DE CONTEÚDO DAS PRINCIPAIS FONTES
        logger.info("📄 EXTRAINDO CONTEÚDO DAS PRINCIPAIS FONTES...")
        extracted_contents = []

        # Combina resultados de todas as buscas
        all_search_results = []
        all_search_results.extend(market_search.get('results', [])[:5])
        all_search_results.extend(audience_search.get('results', [])[:3])
        all_search_results.extend(competition_search.get('results', [])[:4])

        for i, result in enumerate(all_search_results):
            try:
                url = result.get('url', '')
                logger.info(f"📖 Extraindo {i+1}/{len(all_search_results)}: {result.get('title', 'Sem título')}")

                content, metadata = robust_content_extractor.extract_content(url)
                if content and len(content) > 300:
                    extracted_contents.append({
                        'url': url,
                        'title': result.get('title', ''),
                        'content': content,
                        'source_type': 'market_research'
                    })

                time.sleep(0.5)  # Rate limiting

            except Exception as e:
                logger.warning(f"⚠️ Erro ao extrair {url}: {e}")
                continue

        salvar_etapa('conteudo_extraido', {
            'total_extracted': len(extracted_contents),
            'contents': extracted_contents
        }, categoria="analise_completa")

        # 6. ANÁLISE FINAL COM IA
        logger.info("🧠 EXECUTANDO ANÁLISE FINAL COM IA...")

        # Combina todo o conteúdo para análise
        combined_analysis_content = ""

        # Adiciona dados do SupaData
        if supadata_result.get('intelligent_analysis', {}).get('ai_analysis'):
            combined_analysis_content += f"ANÁLISE SUPADATA:\n{supadata_result['intelligent_analysis']['ai_analysis']}\n\n"

        # Adiciona conteúdo extraído
        for content_item in extracted_contents[:8]:  # Top 8 conteúdos
            combined_analysis_content += f"FONTE: {content_item['title']}\n"
            combined_analysis_content += content_item['content'][:2000] + "\n\n"

        # Prompt para análise final
        final_analysis_prompt = f"""
        ANÁLISE ULTRA-DETALHADA DE MERCADO - ARQV30 ENHANCED

        DADOS DO NEGÓCIO:
        - Segmento: {segmento}
        - Produto/Serviço: {produto}  
        - Público-Alvo: {publico}
        - Preço: {context.get('preco', 'N/A')}
        - Objetivo de Receita: {context.get('objetivo_receita', 'N/A')}
        - Orçamento Marketing: {context.get('orcamento_marketing', 'N/A')}
        - Prazo Lançamento: {context.get('prazo_lancamento', 'N/A')}
        - Concorrentes: {context.get('concorrentes', 'N/A')}

        DADOS COLETADOS DA WEB:
        {combined_analysis_content}

        TAREFA:
        Gere uma análise ULTRA-DETALHADA e COMPLETA incluindo:

        1. ANÁLISE DE MERCADO PROFUNDA
        - Tamanho do mercado e potencial
        - Tendências identificadas
        - Oportunidades específicas

        2. ANÁLISE DO PÚBLICO-ALVO
        - Perfil comportamental detalhado
        - Dores e necessidades específicas
        - Canais de comunicação preferenciais

        3. ANÁLISE COMPETITIVA COMPLETA
        - Principais concorrentes identificados
        - Pontos fortes e fracos da concorrência
        - Oportunidades de diferenciação

        4. ESTRATÉGIA DE POSICIONAMENTO
        - Proposta de valor única
        - Messaging framework
        - Diferenciação competitiva

        5. ESTRATÉGIA DE MARKETING
        - Canais de aquisição recomendados
        - Estratégia de conteúdo
        - Cronograma de lançamento

        6. PROJEÇÕES E MÉTRICAS
        - Estimativas de conversão
        - Projeções de receita
        - KPIs recomendados

        7. PLANO DE AÇÃO DETALHADO
        - Próximos passos específicos
        - Timeline de implementação
        - Recursos necessários

        Baseie-se EXCLUSIVAMENTE nos dados coletados e forneça uma análise prática, acionável e extremamente detalhada.
        """

        final_analysis = ai_manager.generate_content(
            prompt=final_analysis_prompt,
            max_tokens=4000,
            temperature=0.2
        )

        salvar_etapa('analise_final_ia', {
            'analysis': final_analysis,
            'prompt_length': len(final_analysis_prompt),
            'response_length': len(final_analysis)
        }, categoria="analise_completa")

        # 7. COMPILA RESULTADO FINAL
        final_result = {
            'success': True,
            'session_id': session_id,
            'analysis_timestamp': datetime.now().isoformat(),
            'input_data': context,
            'data_collection': {
                'supadata_results': supadata_result.get('statistics', {}),
                'web_searches_performed': 3,  # Market, Audience, Competition
                'content_sources_extracted': len(extracted_contents),
                'total_data_quality_score': supadata_result.get('supadata_collection', {}).get('data_quality_score', 0)
            },
            'final_analysis': final_analysis,
            'supporting_data': {
                'market_search_results': len(market_search.get('results', [])),
                'audience_search_results': len(audience_search.get('results', [])),
                'competition_search_results': len(competition_search.get('results', [])),
                'extracted_content_sources': [
                    {'title': c['title'], 'url': c['url']} 
                    for c in extracted_contents
                ]
            },
            'metadata': {
                'analysis_engine': 'ARQV30_Enhanced_v2_REAL',
                'webscraping_performed': True,
                'supadata_used': True,
                'content_extraction_performed': True,
                'ai_analysis_performed': True
            }
        }

        salvar_etapa('resultado_final_completo', final_result, categoria="analise_completa")

        logger.info(f"✅ ANÁLISE REAL CONCLUÍDA: {session_id}")

        return jsonify(final_result)

    except Exception as e:
        logger.error(f"❌ ERRO CRÍTICO na análise {session_id}: {str(e)}", exc_info=True)

        salvar_erro('analise_critica', e, contexto={
            'session_id': session_id,
            'form_data': form_data if 'form_data' in locals() else {}
        })

        return jsonify({
            'success': False,
            'error': f'Erro crítico na análise: {str(e)}',
            'session_id': session_id,
            'timestamp': datetime.now().isoformat()
        }), 500

@enhanced_analysis_bp.route('/status/<session_id>', methods=['GET'])
def get_analysis_status(session_id):
    """Retorna status de uma análise específica"""

    try:
        # Status básico - poderia ser expandido com sistema de cache
        return jsonify({
            'session_id': session_id,
            'status': 'completed',  # Por simplicidade, sempre completed
            'timestamp': datetime.now().isoformat(),
            'systems_status': {
                'unified_search': unified_search_manager.get_provider_status(),
                'content_extractor': robust_content_extractor.get_stats(),
                'supadata_manager': mcp_supadata_manager.get_status(),
                'ai_manager': ai_manager.get_provider_status()
            }
        })

    except Exception as e:
        logger.error(f"❌ Erro ao obter status {session_id}: {e}")
        return jsonify({
            'error': str(e),
            'session_id': session_id
        }), 500