#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ARQV30 Enhanced v2.0 - Consolidação Final Ultra-Robusta
Sistema de consolidação que NUNCA falha e sempre gera relatório
"""

import os
import logging
import time
import json
from datetime import datetime
from typing import Dict, List, Any, Optional
from pathlib import Path
from services.auto_save_manager import auto_save_manager, salvar_etapa, salvar_erro
from services.ai_manager import ai_manager

logger = logging.getLogger(__name__)

class ConsolidacaoFinal:
    """Sistema de consolidação final ultra-robusto"""

    def __init__(self):
        """Inicializa o sistema de consolidação"""
        self.backup_dir = Path("backups")
        self.backup_dir.mkdir(exist_ok=True)
        self.auto_save = auto_save_manager
        logger.info("Sistema de consolidação final inicializado")

    def consolidar_analise_completa(self, dados_pipeline: Dict[str, Any], session_id: str) -> Dict[str, Any]:
        """Consolida análise completa com fallbacks robustos"""

        try:
            logger.info(f"🔄 Iniciando consolidação final para sessão: {session_id}")

            # Valida dados de entrada
            if not dados_pipeline:
                logger.warning("⚠️ Dados do pipeline vazios, gerando relatório de emergência")
                return self._gerar_relatorio_emergencia(session_id, "Dados do pipeline vazios")

            # Gera relatório consolidado
            relatorio_final = self._gerar_relatorio_consolidado(dados_pipeline, session_id)

            # Salva resultado final
            salvar_etapa("consolidacao_final", relatorio_final, categoria="analise_completa")

            logger.info("✅ Consolidação final concluída com sucesso")
            return relatorio_final

        except Exception as e:
            logger.error(f"❌ Erro na consolidação final: {e}")
            salvar_erro("consolidacao_final", e)

            # Retorna relatório de emergência
            return self._gerar_relatorio_emergencia(session_id, str(e))

    def _gerar_relatorio_consolidado(self, dados: Dict[str, Any], session_id: str) -> Dict[str, Any]:
        """Gera relatório consolidado"""

        # Extrai componentes principais
        avatar = dados.get('avatar_ultra_detalhado', {})
        drivers = dados.get('drivers_mentais_customizados', {})
        provas = dados.get('provas_visuais_sugeridas', [])
        pesquisa = dados.get('pesquisa_web_massiva', {})
        insights = dados.get('insights_exclusivos', [])

        # Calcula métricas de completude
        componentes_presentes = sum([
            bool(avatar),
            bool(drivers),
            bool(provas),
            bool(pesquisa),
            bool(insights)
        ])

        completude = (componentes_presentes / 5) * 100

        relatorio_consolidado = {
            'session_id': session_id,
            'timestamp': datetime.now().isoformat(),
            'tipo': 'analise_consolidada',
            'metadados': {
                'componentes_presentes': componentes_presentes,
                'completude_percentual': completude,
                'status_qualidade': 'Alta' if completude >= 80 else 'Média' if completude >= 60 else 'Baixa'
            },
            'avatar_ultra_detalhado': avatar,
            'drivers_mentais_customizados': drivers,
            'provas_visuais_sugeridas': provas,
            'sistema_anti_objecao': dados.get('sistema_anti_objecao', {}),
            'pesquisa_web_massiva': pesquisa,
            'insights_exclusivos': insights,
            'analise_concorrencia_detalhada': dados.get('analise_concorrencia_detalhada', {}),
            'estrategia_palavras_chave': dados.get('estrategia_palavras_chave', {}),
            'metricas_performance_detalhadas': dados.get('metricas_performance_detalhadas', {}),
            'plano_acao_detalhado': dados.get('plano_acao_detalhado', {}),
            'funil_vendas_detalhado': dados.get('funil_vendas_detalhado', {}),
            'predicoes_futuro_completas': dados.get('predicoes_futuro_completas', {}),
            'pre_pitch_invisivel': dados.get('pre_pitch_invisivel', {}),
            'status': 'sucesso'
        }

        return relatorio_consolidado

    def _gerar_relatorio_emergencia(self, session_id: str, erro: str) -> Dict[str, Any]:
        """Gera relatório de emergência quando consolidação principal falha"""

        try:
            logger.warning(f"🆘 Gerando relatório de emergência para sessão: {session_id}")

            relatorio_emergencia = {
                'session_id': session_id,
                'timestamp': datetime.now().isoformat(),
                'tipo': 'emergencia_critica',
                'erro': erro,
                'status': 'erro',
                'dados_emergencia': {
                    'avatar_ultra_detalhado': self._gerar_avatar_emergencia(),
                    'drivers_mentais_customizados': self._gerar_drivers_emergencia(),
                    'insights_exclusivos': self._gerar_insights_emergencia(),
                    'recomendacoes_emergencia': [
                        'Configure as APIs necessárias para análise completa',
                        'Verifique conectividade com serviços externos',
                        'Tente novamente com dados mais específicos'
                    ]
                },
                'recuperacao_possivel': True,
                'proximos_passos': [
                    'Revisar configuração de APIs',
                    'Verificar logs detalhados',
                    'Executar nova análise'
                ]
            }

            # Salva relatório de emergência
            salvar_etapa("relatorio_emergencia", relatorio_emergencia, categoria="analise_completa")

            return relatorio_emergencia

        except Exception as final_error:
            # Último recurso - retorna estrutura mínima
            logger.critical(f"🚨 Fallback absoluto falhou: {final_error}")

            return {
                'tipo': 'emergencia_critica',
                'session_id': session_id,
                'timestamp': datetime.now().isoformat(),
                'erro': f"Erro crítico: {erro}, Fallback falhou: {final_error}",
                'status': 'erro_critico',
                'recuperacao_possivel': False
            }

    def _gerar_avatar_emergencia(self) -> Dict[str, Any]:
        """Gera avatar básico de emergência"""

        return {
            'nome_ficticio': 'Cliente Profissional',
            'perfil_demografico': {
                'idade': '35-45 anos',
                'renda': 'Classe média alta',
                'escolaridade': 'Superior completo',
                'localizacao': 'Brasil - Grandes centros urbanos'
            },
            'dores_viscerais': [
                'Falta de tempo para focar no que importa',
                'Dificuldade em obter resultados consistentes',
                'Sobrecarga de informações conflitantes',
                'Pressão por resultados rápidos'
            ],
            'desejos_secretos': [
                'Ser reconhecido como referência em sua área',
                'Ter mais tempo livre para família',
                'Alcançar independência financeira',
                'Fazer diferença positiva no mundo'
            ],
            'observacao': 'Avatar gerado em modo de emergência - Configure APIs para análise detalhada'
        }

    def _gerar_drivers_emergencia(self) -> Dict[str, Any]:
        """Gera drivers básicos de emergência"""

        return {
            'drivers_customizados': [
                {
                    'nome': 'Urgência Temporal',
                    'gatilho_central': 'Escassez de tempo',
                    'roteiro_ativacao': {
                        'historia_analogia': 'Como um executivo que perdeu oportunidades por não agir rapidamente',
                        'metafora_visual': 'Trem que está partindo da estação',
                        'comando_acao': 'Não deixe esta oportunidade passar'
                    }
                },
                {
                    'nome': 'Prova Social',
                    'gatilho_central': 'Validação pelos pares',
                    'roteiro_ativacao': {
                        'historia_analogia': 'Outros profissionais já estão obtendo resultados',
                        'metafora_visual': 'Multidão caminhando na mesma direção',
                        'comando_acao': 'Junte-se aos que já estão na frente'
                    }
                }
            ],
            'observacao': 'Drivers gerados em modo de emergência - Configure APIs para personalização completa'
        }

    def _gerar_insights_emergencia(self) -> List[str]:
        """Gera insights básicos de emergência"""

        return [
            'O mercado brasileiro está em constante evolução e demanda soluções inovadoras',
            'Profissionais que se antecipam às tendências obtêm vantagem competitiva',
            'A personalização é fundamental para o sucesso em qualquer segmento',
            'Dados específicos são essenciais para tomadas de decisão assertivas',
            'Configure as APIs necessárias para obter análises mais detalhadas'
        ]

# Instância global
consolidacao_final = ConsolidacaoFinal()