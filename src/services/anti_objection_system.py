#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ARQV30 Enhanced v2.0 - Anti Objection System
Sistema anti-objeção com arsenal completo
"""

import logging
import json
from typing import Dict, List, Any, Optional
from .ai_manager import QuantumAIManager
from .auto_save_manager import auto_save_manager

logger = logging.getLogger(__name__)

class AntiObjectionSystem:
    """Sistema Anti-Objeção com Arsenal Completo"""

    def __init__(self):
        """Inicializa o sistema anti-objeção"""
        self.ai_manager = QuantumAIManager()
        self.auto_save = AutoSaveManager("anti_objecao")

        # Arsenal de objeções comuns
        self.common_objections = {
            "preco": [
                "Está muito caro",
                "Não tenho dinheiro agora",
                "Preciso pensar no investimento"
            ],
            "tempo": [
                "Não tenho tempo",
                "Estou muito ocupado",
                "Talvez mais tarde"
            ],
            "confianca": [
                "Não conheço vocês",
                "Preciso pesquisar mais",
                "Já fui enganado antes"
            ],
            "necessidade": [
                "Não preciso disso",
                "Já tenho algo parecido",
                "Não é prioridade agora"
            ],
            "decisao": [
                "Preciso conversar com minha esposa",
                "Não decido sozinho",
                "Vou pensar"
            ]
        }

        logger.info("Anti-Objection System inicializado com arsenal completo")

    def generate_anti_objection_system(self, product_data: Dict[str, Any]) -> Dict[str, Any]:
        """Gera sistema anti-objeção personalizado"""

        try:
            logger.info("🛡️ Gerando sistema anti-objeção para 5 objeções")

            # Salvar dados de entrada
            self.auto_save.save_stage("anti_objecao_entrada", product_data)

            # Identificar objeções principais
            main_objections = self._identify_main_objections(product_data)

            # Salvar objeções analisadas
            self.auto_save.save_stage("objecoes_analisadas", {"objections": main_objections})

            # Gerar contra-ataques
            counter_attacks = self._generate_counter_attacks(main_objections, product_data)

            # Salvar contra-ataques
            self.auto_save.save_stage("contra_ataques", counter_attacks)

            # Gerar scripts personalizados
            try:
                personalized_scripts = self._generate_personalized_scripts(counter_attacks, product_data)
            except Exception as e:
                logger.error(f"❌ Erro crítico ao gerar scripts personalizados: {e}")
                self.auto_save.save_stage("ERRO_scripts_personalizados", {"error": str(e)})
                personalized_scripts = self._create_basic_scripts(product_data)

            # Sistema completo
            anti_objection_system = {
                "main_objections": main_objections,
                "counter_attacks": counter_attacks,
                "personalized_scripts": personalized_scripts,
                "objection_prevention": self._generate_objection_prevention(product_data),
                "psychological_triggers": self._generate_psychological_triggers(product_data)
            }

            logger.info("✅ Sistema anti-objeção gerado com sucesso")
            return anti_objection_system

        except Exception as e:
            logger.error(f"❌ Erro ao gerar sistema anti-objeção: {e}")
            self.auto_save.save_stage("ERRO_anti_objecao_sistema", {"error": str(e)})

            # Retornar sistema básico
            logger.warning("🔄 Gerando sistema anti-objeção básico como fallback...")
            return self._create_basic_anti_objection_system(product_data)

    def _identify_main_objections(self, product_data: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Identifica as principais objeções para o produto"""

        segment = product_data.get('segmento', 'Geral')
        price_range = product_data.get('preco', 'Não informado')

        # Objeções baseadas no segmento
        main_objections = []

        if 'medicina' in segment.lower() or 'medico' in segment.lower():
            main_objections = [
                {
                    "type": "confianca",
                    "objection": "Não confio em cursos online para área médica",
                    "frequency": "Alta",
                    "intensity": "Forte"
                },
                {
                    "type": "tempo",
                    "objection": "Não tenho tempo com minha agenda médica",
                    "frequency": "Muito Alta",
                    "intensity": "Muito Forte"
                },
                {
                    "type": "preco",
                    "objection": "Já invisto muito em congressos e cursos",
                    "frequency": "Alta",
                    "intensity": "Moderada"
                },
                {
                    "type": "necessidade",
                    "objection": "Já sei telemedicina na prática",
                    "frequency": "Moderada",
                    "intensity": "Forte"
                },
                {
                    "type": "regulamentacao",
                    "objection": "As regras de telemedicina mudam muito",
                    "frequency": "Alta",
                    "intensity": "Forte"
                }
            ]
        else:
            # Objeções genéricas
            main_objections = [
                {"type": "preco", "objection": "Está muito caro", "frequency": "Alta", "intensity": "Forte"},
                {"type": "tempo", "objection": "Não tenho tempo", "frequency": "Muito Alta", "intensity": "Forte"},
                {"type": "confianca", "objection": "Não conheço vocês", "frequency": "Moderada", "intensity": "Moderada"},
                {"type": "necessidade", "objection": "Não preciso disso agora", "frequency": "Alta", "intensity": "Moderada"},
                {"type": "decisao", "objection": "Preciso pensar", "frequency": "Muito Alta", "intensity": "Fraca"}
            ]

        return main_objections

    def _generate_counter_attacks(self, objections: List[Dict[str, Any]], product_data: Dict[str, Any]) -> Dict[str, Any]:
        """Gera contra-ataques para cada objeção"""

        counter_attacks = {}

        for objection in objections:
            obj_type = objection["type"]
            obj_text = objection["objection"]

            if obj_type == "confianca":
                counter_attacks[obj_type] = {
                    "immediate_response": "Entendo perfeitamente sua preocupação. Deixe-me mostrar nossos resultados...",
                    "evidence": [
                        "Depoimentos de médicos que já fizeram o curso",
                        "Certificações e credenciais da instituição",
                        "Casos de sucesso documentados"
                    ],
                    "reframe": "Na verdade, sua prudência mostra que você é um profissional sério"
                }
            elif obj_type == "tempo":
                counter_attacks[obj_type] = {
                    "immediate_response": "Dr., justamente por isso criamos um método que se adapta à sua agenda",
                    "evidence": [
                        "Aulas de 15-20 minutos",
                        "Acesso vitalício para estudar quando puder",
                        "App mobile para estudar entre consultas"
                    ],
                    "reframe": "O tempo que investe agora vai economizar horas no futuro"
                }
            elif obj_type == "preco":
                counter_attacks[obj_type] = {
                    "immediate_response": "Vou te mostrar como esse investimento se paga sozinho",
                    "evidence": [
                        "ROI médio de 300% no primeiro mês",
                        "Economia de tempo vale mais que o investimento",
                        "Parcelamento sem juros disponível"
                    ],
                    "reframe": "Não é um gasto, é um investimento no seu futuro profissional"
                }
            else:
                counter_attacks[obj_type] = {
                    "immediate_response": f"Entendo sua preocupação sobre {obj_text}",
                    "evidence": ["Evidência personalizada será gerada"],
                    "reframe": "Vamos ver isso de outra perspectiva"
                }

        return counter_attacks

    def _generate_personalized_scripts(self, counter_attacks: Dict[str, Any], product_data: Dict[str, Any]) -> Dict[str, Any]:
        """Gera scripts personalizados usando IA"""

        prompt = f"""
        Crie scripts de vendas personalizados para superar objeções no segmento: {product_data.get('segmento', 'Geral')}

        Produto: {product_data.get('produto', 'Produto/Serviço')}
        Público: {product_data.get('publico', 'Profissionais')}

        Para cada objeção, crie:
        1. Script de resposta imediata (30-60 segundos)
        2. Apresentação de evidências (1-2 minutos) 
        3. Fechamento com reframe (30 segundos)

        Objeções principais:
        {json.dumps(list(counter_attacks.keys()), indent=2)}

        Retorne em formato JSON estruturado.
        """

        try:
            response = self.ai_manager.generate_content(prompt, max_length=3000)

            # Tentar parsear JSON
            try:
                scripts = json.loads(response)
                return scripts
            except json.JSONDecodeError:
                logger.warning("⚠️ IA retornou JSON inválido para scripts")
                return self._create_basic_scripts(product_data)

        except Exception as e:
            logger.error(f"❌ Erro ao gerar scripts com IA: {e}")
            return self._create_basic_scripts(product_data)

    def _create_basic_scripts(self, product_data: Dict[str, Any]) -> Dict[str, Any]:
        """Cria scripts básicos quando a IA falha"""

        segment = product_data.get('segmento', 'Geral')

        if 'medic' in segment.lower():
            return {
                "confianca": {
                    "script": "Dr., entendo sua preocupação. Somos reconhecidos pelo CFM e temos mais de 500 médicos formados.",
                    "evidencias": "Mostrar certificações e depoimentos",
                    "fechamento": "Sua prudência mostra que você fará bom uso do conhecimento"
                },
                "tempo": {
                    "script": "Criamos especificamente para médicos ocupados. São apenas 15 min por dia.",
                    "evidencias": "Demonstrar flexibilidade da plataforma",
                    "fechamento": "O tempo investido agora economizará horas no futuro"
                },
                "preco": {
                    "script": "Vou mostrar como se paga sozinho na primeira consulta de telemedicina.",
                    "evidencias": "Calcular ROI baseado na prática médica",
                    "fechamento": "É um investimento, não um gasto"
                }
            }

        return {
            "genericos": {
                "script": "Entendo sua preocupação. Vamos esclarecer isso juntos.",
                "evidencias": "Apresentar dados relevantes",
                "fechamento": "Agora faz mais sentido?"
            }
        }

    def _generate_objection_prevention(self, product_data: Dict[str, Any]) -> Dict[str, Any]:
        """Gera estratégias para prevenir objeções"""

        return {
            "opening_statements": [
                "Antes de começar, quero esclarecer os pontos que mais geram dúvidas",
                "Vou ser transparente sobre tudo desde o início",
                "Deixe-me mostrar exatamente o que você está recebendo"
            ],
            "social_proof": [
                "Mais de 500 profissionais já transformaram suas carreiras",
                "Dr. João Silva aumentou sua renda em 40% no primeiro mês",
                "Reconhecido pelas principais entidades médicas"
            ],
            "urgency_builders": [
                "As vagas são limitadas para manter a qualidade",
                "O preço promocional acaba em 48 horas",
                "A próxima turma só abre em 3 meses"
            ]
        }

    def _generate_psychological_triggers(self, product_data: Dict[str, Any]) -> Dict[str, Any]:
        """Gera gatilhos psicológicos para superar resistências"""

        return {
            "reciprocidade": [
                "Oferecer conteúdo gratuito antes de vender",
                "Compartilhar informações valiosas",
                "Dar algo de valor sem pedir nada"
            ],
            "autoridade": [
                "Credenciais e experiência do instrutor",
                "Reconhecimentos e prêmios",
                "Casos de sucesso documentados"
            ],
            "escassez": [
                "Vagas limitadas",
                "Oferta por tempo limitado",
                "Exclusividade do grupo"
            ],
            "consistencia": [
                "Fazer micro-compromissos",
                "Confirmar interesse e necessidade",
                "Criar senso de compromisso"
            ]
        }

    def _create_basic_anti_objection_system(self, product_data: Dict[str, Any]) -> Dict[str, Any]:
        """Cria sistema anti-objeção básico"""

        return {
            "main_objections": [
                {"type": "preco", "objection": "Está caro", "frequency": "Alta"},
                {"type": "tempo", "objection": "Sem tempo", "frequency": "Alta"},
                {"type": "confianca", "objection": "Não conheço", "frequency": "Moderada"}
            ],
            "counter_attacks": {
                "preco": {"response": "Vou mostrar o ROI", "evidence": ["Calculadora de retorno"]},
                "tempo": {"response": "Flexível e prático", "evidence": ["Acesso mobile"]},
                "confianca": {"response": "Somos reconhecidos", "evidence": ["Certificações"]}
            },
            "scripts": self._create_basic_scripts(product_data),
            "prevention": {"social_proof": ["Depoimentos", "Casos de sucesso"]},
            "triggers": {"urgency": ["Vagas limitadas"], "authority": ["Especialistas"]}
        }

    def generate_complete_anti_objection_system(self, objections_list: List[str], avatar_data: Dict[str, Any], context_data: Dict[str, Any]) -> Dict[str, Any]:
        """Gera sistema anti-objeção completo para o unified analysis engine"""
        try:
            logger.info("🛡️ Gerando sistema anti-objeção completo")

            # Usar dados do contexto como product_data
            product_data = {
                'segmento': context_data.get('segmento', 'Geral'),
                'produto': context_data.get('produto', 'Produto/Serviço'),
                'publico': context_data.get('publico', 'Profissionais'),
                'preco': context_data.get('preco', 'Não informado')
            }

            # Identificar objeções principais
            main_objections = self._identify_main_objections(product_data)

            # Adicionar objeções customizadas da lista
            for objection in objections_list[:5]:  # Máximo 5 objeções
                main_objections.append({
                    "type": "custom",
                    "objection": objection,
                    "frequency": "Alta",
                    "intensity": "Forte"
                })

            # Gerar contra-ataques
            counter_attacks = self._generate_counter_attacks(main_objections, product_data)

            # Gerar scripts personalizados
            try:
                personalized_scripts = self._generate_personalized_scripts(counter_attacks, product_data)
            except Exception as e:
                logger.error(f"❌ Erro ao gerar scripts: {e}")
                personalized_scripts = self._create_basic_scripts(product_data)

            # Sistema completo
            complete_system = {
                "main_objections": main_objections,
                "counter_attacks": counter_attacks,
                "personalized_scripts": personalized_scripts,
                "objection_prevention": self._generate_objection_prevention(product_data),
                "psychological_triggers": self._generate_psychological_triggers(product_data),
                "avatar_integration": {
                    "avatar_fears": avatar_data.get('medos_profundos', []),
                    "avatar_desires": avatar_data.get('aspiracoes_secretas', []),
                    "targeted_responses": self._create_avatar_targeted_responses(avatar_data)
                }
            }

            logger.info("✅ Sistema anti-objeção completo gerado")
            return complete_system

        except Exception as e:
            logger.error(f"❌ Erro no sistema anti-objeção completo: {e}")
            return self._create_basic_anti_objection_system(product_data)

    def _create_avatar_targeted_responses(self, avatar_data: Dict[str, Any]) -> Dict[str, Any]:
        """Cria respostas direcionadas baseadas no avatar"""
        return {
            "fear_based_responses": [
                f"Entendo que você possa ter receio sobre {fear}" 
                for fear in avatar_data.get('medos_profundos', ['investir sem garantias'])[:3]
            ],
            "desire_based_responses": [
                f"Imagino que você sonha em {desire}" 
                for desire in avatar_data.get('aspiracoes_secretas', ['ter sucesso profissional'])[:3]
            ],
            "personality_match": {
                "communication_style": avatar_data.get('personalidade', 'Direto e objetivo'),
                "trust_builders": ["Dados concretos", "Casos reais", "Garantias sólidas"]
            }
        }

# Instância global para ser importada
anti_objection_system = AntiObjectionSystem()