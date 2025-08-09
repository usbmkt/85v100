#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ARQV30 Enhanced v2.0 - Mental Drivers Architect
Arquiteto de Drivers Mentais Customizados
"""

import time
import random
import logging
import json
from typing import Dict, List, Any, Optional
from services.ai_manager import ai_manager
from services.auto_save_manager import salvar_etapa, salvar_erro

logger = logging.getLogger(__name__)

class MentalDriversArchitect:
    """Arquiteto de Drivers Mentais Customizados"""
    
    def __init__(self):
        """Inicializa o arquiteto"""
        self.ai_manager = ai_manager
        logger.info("Mental Drivers Architect inicializado")
    
    def generate_custom_mental_drivers(self, context_data: Dict[str, Any], avatar_data: Dict[str, Any]) -> Dict[str, Any]:
        """Gera drivers mentais customizados"""
        try:
            logger.info("🧠 Gerando drivers mentais customizados")
            
            # Drivers básicos sempre incluídos
            basic_drivers = {
                "urgencia": {
                    "nome": "Urgência",
                    "descricao": "Cria sensação de que a oportunidade é limitada no tempo",
                    "aplicacao": "Oferta por tempo limitado com countdown visível"
                },
                "escassez": {
                    "nome": "Escassez",
                    "descricao": "Destaca a limitação de quantidade ou disponibilidade",
                    "aplicacao": "Apenas X vagas disponíveis"
                },
                "autoridade": {
                    "nome": "Autoridade",
                    "descricao": "Demonstra expertise e credibilidade",
                    "aplicacao": "Depoimentos de especialistas e certificações"
                },
                "prova_social": {
                    "nome": "Prova Social",
                    "descricao": "Mostra que outros já fizeram e tiveram sucesso",
                    "aplicacao": "Cases de clientes reais com resultados"
                }
            }
            
            return {
                "status": "sucesso",
                "drivers_customizados": basic_drivers,
                "total_drivers": len(basic_drivers)
            }
            
        except Exception as e:
            logger.error(f"❌ Erro ao gerar drivers mentais: {e}")
            salvar_erro("drivers_mentais", e, {"context": context_data})
            return {
                "status": "erro",
                "drivers_customizados": {},
                "total_drivers": 0
            }

# Instância global
mental_drivers_architect = MentalDriversArchitect()

class MentalDriversArchitect:
    """Arquiteto de Drivers Mentais Customizados"""
    
    def __init__(self):
        """Inicializa o arquiteto de drivers mentais"""
        self.universal_drivers = self._load_universal_drivers()
        self.driver_templates = self._load_driver_templates()
        
        logger.info("Mental Drivers Architect inicializado")
    
    def _load_universal_drivers(self) -> Dict[str, Dict[str, Any]]:
        """Carrega os 19 drivers mentais universais completos"""
        return {
            # DRIVERS EMOCIONAIS PRIMÁRIOS
            'ferida_exposta': {
                'nome': 'Ferida Exposta',
                'gatilho_central': 'Dor não resolvida',
                'definicao_visceral': 'Trazer à consciência o que foi reprimido',
                'mecanica_psicologica': 'Ativa sistema límbico de alerta e urgência',
                'ativacao': 'Você ainda [comportamento doloroso] mesmo sabendo que [consequência]?',
                'categoria': 'emocional_primario'
            },
            'trofeu_secreto': {
                'nome': 'Troféu Secreto',
                'gatilho_central': 'Desejo inconfessável',
                'definicao_visceral': 'Validar ambições "proibidas"',
                'mecanica_psicologica': 'Libera dopamina através de permissão social',
                'ativacao': 'Não é sobre dinheiro, é sobre [desejo real oculto]',
                'categoria': 'emocional_primario'
            },
            'inveja_produtiva': {
                'nome': 'Inveja Produtiva',
                'gatilho_central': 'Comparação com pares',
                'definicao_visceral': 'Transformar inveja em combustível',
                'mecanica_psicologica': 'Converte energia negativa em motivação de ação',
                'ativacao': 'Enquanto você [situação atual], outros como você [resultado desejado]',
                'categoria': 'emocional_primario'
            },
            'relogio_psicologico': {
                'nome': 'Relógio Psicológico',
                'gatilho_central': 'Urgência existencial',
                'definicao_visceral': 'Tempo como recurso finito e em escassez',
                'mecanica_psicologica': 'Ativa cortisol de urgência temporal',
                'ativacao': 'Quantos [período] você ainda vai [desperdício]?',
                'categoria': 'emocional_primario'
            },
            'identidade_aprisionada': {
                'nome': 'Identidade Aprisionada',
                'gatilho_central': 'Conflito entre quem é e quem poderia ser',
                'definicao_visceral': 'Expor a máscara social limitante',
                'mecanica_psicologica': 'Cria dissonância cognitiva forçando mudança',
                'ativacao': 'Você não é [rótulo limitante], você é [potencial real]',
                'categoria': 'emocional_primario'
            },
            'custo_invisivel': {
                'nome': 'Custo Invisível',
                'gatilho_central': 'Perda não percebida',
                'definicao_visceral': 'Quantificar o preço da inação',
                'mecanica_psicologica': 'Torna perdas abstratas em dor concreta',
                'ativacao': 'Cada dia sem [solução] custa [perda específica]',
                'categoria': 'emocional_primario'
            },
            'ambicao_expandida': {
                'nome': 'Ambição Expandida',
                'gatilho_central': 'Sonhos pequenos demais',
                'definicao_visceral': 'Elevar o teto mental de possibilidades',
                'mecanica_psicologica': 'Expande neuroplasticidade de visão de futuro',
                'ativacao': 'Se o esforço é o mesmo, por que você está pedindo tão pouco?',
                'categoria': 'emocional_primario'
            },
            'diagnostico_brutal': {
                'nome': 'Diagnóstico Brutal',
                'gatilho_central': 'Confronto com a realidade atual',
                'definicao_visceral': 'Criar indignação produtiva com status quo',
                'mecanica_psicologica': 'Quebra negação através de evidência irrefutável',
                'ativacao': 'Olhe seus números/situação. Até quando você vai aceitar isso?',
                'categoria': 'emocional_primario'
            },
            'ambiente_vampiro': {
                'nome': 'Ambiente Vampiro',
                'gatilho_central': 'Consciência do entorno tóxico',
                'definicao_visceral': 'Revelar como ambiente atual suga energia/potencial',
                'mecanica_psicologica': 'Identifica drenos externos de energia',
                'ativacao': 'Seu ambiente te impulsiona ou te mantém pequeno?',
                'categoria': 'emocional_primario'
            },
            'mentor_salvador': {
                'nome': 'Mentor Salvador',
                'gatilho_central': 'Necessidade de orientação externa',
                'definicao_visceral': 'Ativar desejo por figura de autoridade que acredita neles',
                'mecanica_psicologica': 'Ativa circuito neurológico de busca por proteção',
                'ativacao': 'Você precisa de alguém que veja seu potencial quando você não consegue',
                'categoria': 'emocional_primario'
            },
            'coragem_necessaria': {
                'nome': 'Coragem Necessária',
                'gatilho_central': 'Medo paralisante disfarçado',
                'definicao_visceral': 'Transformar desculpas em decisões corajosas',
                'mecanica_psicologica': 'Converte adrenalina do medo em ação',
                'ativacao': 'Não é sobre condições perfeitas, é sobre decidir apesar do medo',
                'categoria': 'emocional_primario'
            },
            
            # DRIVERS RACIONAIS COMPLEMENTARES
            'mecanismo_revelado': {
                'nome': 'Mecanismo Revelado',
                'gatilho_central': 'Compreensão do "como"',
                'definicao_visceral': 'Desmistificar o complexo',
                'mecanica_psicologica': 'Ativa córtex pré-frontal de compreensão',
                'ativacao': 'É simplesmente [analogia simples], não [complicação percebida]',
                'categoria': 'racional_complementar'
            },
            'prova_matematica': {
                'nome': 'Prova Matemática',
                'gatilho_central': 'Certeza numérica',
                'definicao_visceral': 'Equação irrefutável',
                'mecanica_psicologica': 'Satisfaz necessidade de lógica do cérebro racional',
                'ativacao': 'Se você fizer X por Y dias = Resultado Z garantido',
                'categoria': 'racional_complementar'
            },
            'padrao_oculto': {
                'nome': 'Padrão Oculto',
                'gatilho_central': 'Insight revelador',
                'definicao_visceral': 'Mostrar o que sempre esteve lá',
                'mecanica_psicologica': 'Cria momento "eureka" de descoberta',
                'ativacao': 'Todos que conseguiram [resultado] fizeram [padrão específico]',
                'categoria': 'racional_complementar'
            },
            'excecao_possivel': {
                'nome': 'Exceção Possível',
                'gatilho_central': 'Quebra de limitação',
                'definicao_visceral': 'Provar que regras podem ser quebradas',
                'mecanica_psicologica': 'Expande limites de crença sobre possibilidades',
                'ativacao': 'Diziam que [limitação], mas [prova contrária]',
                'categoria': 'racional_complementar'
            },
            'atalho_etico': {
                'nome': 'Atalho Ético',
                'gatilho_central': 'Eficiência sem culpa',
                'definicao_visceral': 'Validar o caminho mais rápido',
                'mecanica_psicologica': 'Remove culpa social de buscar facilidade',
                'ativacao': 'Por que sofrer [tempo longo] se existe [atalho comprovado]?',
                'categoria': 'racional_complementar'
            },
            'decisao_binaria': {
                'nome': 'Decisão Binária',
                'gatilho_central': 'Simplificação radical',
                'definicao_visceral': 'Eliminar zona cinzenta',
                'mecanica_psicologica': 'Força circuito de decisão através de simplicidade',
                'ativacao': 'Ou você [ação desejada] ou aceita [consequência dolorosa]',
                'categoria': 'racional_complementar'
            },
            'oportunidade_oculta': {
                'nome': 'Oportunidade Oculta',
                'gatilho_central': 'Vantagem não percebida',
                'definicao_visceral': 'Revelar demanda/chance óbvia mas ignorada',
                'mecanica_psicologica': 'Ativa sistema de recompensa por descoberta',
                'ativacao': 'O mercado está gritando por [solução] e ninguém está ouvindo',
                'categoria': 'racional_complementar'
            },
            'metodo_vs_sorte': {
                'nome': 'Método vs Sorte',
                'gatilho_central': 'Caos vs sistema',
                'definicao_visceral': 'Contrastar tentativa aleatória com caminho estruturado',
                'mecanica_psicologica': 'Ativa preferência neurológica por ordem e previsibilidade',
                'ativacao': 'Sem método você está cortando mata com foice. Com método, está na autoestrada',
                'categoria': 'racional_complementar'
            }
        }
    
    def _load_driver_templates(self) -> Dict[str, str]:
        """Carrega templates expandidos de drivers"""
        return {
            'historia_analogia': 'Era uma vez {personagem} que enfrentava {problema_similar}. Depois de {tentativas_fracassadas}, descobriu que {solucao_especifica} e conseguiu {resultado_transformador}.',
            'metafora_visual': 'Imagine {situacao_atual} como {metafora_visual}. Agora visualize {situacao_ideal} como {metafora_transformada}.',
            'comando_acao': 'Agora que você {compreensao_adquirida}, a única ação lógica é {acao_especifica} porque {consequencia_inevitavel}.',
            
            # TEMPLATES AVANÇADOS
            'pergunta_ferida': 'Você ainda {comportamento_doloroso} mesmo sabendo que {consequencia_terrivel}?',
            'confronto_brutal': 'Deixa eu te fazer uma pergunta difícil sobre {area_vida}...',
            'calculo_perda': 'Cada {periodo_tempo} sem {solucao} = {perda_quantificada} perdidos para sempre',
            'comparacao_cruel': 'Enquanto você {situacao_atual_patética}, outros como você {resultado_invejavel}',
            'urgencia_temporal': 'Quantos {periodo} você ainda vai {desperdicio} antes de {acao_necessaria}?',
            'identidade_expandida': 'Você não é {rotulo_limitante}, você é {potencial_real_gigante}',
            'ambiente_toxico': 'Seu {ambiente_especifico} te impulsiona ou te mantém {limitacao}?',
            'mentor_necessario': 'Você precisa de alguém que {apoio_especifico} quando você {momento_fraqueza}',
            'coragem_vs_desculpa': 'Não é sobre {condicao_perfeita}, é sobre {decisao_corajosa}',
            'mecanismo_simples': 'É simplesmente {analogia_simples}, não {complicacao_falsa}',
            'prova_numerica': 'Se você {acao_X} por {tempo_Y} = {resultado_Z} matematicamente garantido',
            'padrao_universal': 'TODOS que conseguiram {resultado_desejado} fizeram {padrao_especifico}',
            'quebra_regra': 'Diziam que {limitacao_aceita}, mas {prova_contraria_irrefutavel}',
            'atalho_validado': 'Por que {sofrimento_longo} se existe {caminho_rapido_comprovado}?',
            'binario_radical': 'Ou você {acao_desejada} AGORA ou aceita {consequencia_dolorosa} para sempre',
            'chance_invisivel': 'O mercado está GRITANDO por {solucao} e ninguém está OUVINDO',
            'sistema_vs_caos': 'Sem método = {metafora_caos}. Com método = {metafora_autoestrada}'
        }
    
    def generate_complete_drivers_system(
        self, 
        avatar_data: Dict[str, Any], 
        context_data: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Gera sistema completo de drivers mentais customizados"""
        
        # Validação e correção de entrada
        if not avatar_data:
            logger.warning("⚠️ Dados do avatar ausentes, criando avatar básico")
            avatar_data = self._create_basic_avatar(context_data)
        
        if not context_data.get('segmento'):
            logger.warning("⚠️ Segmento não informado, usando padrão")
            context_data['segmento'] = 'Negócios'
        
        try:
            logger.info("🧠 Gerando drivers mentais customizados...")
            
            # Salva dados de entrada imediatamente
            salvar_etapa("drivers_entrada", {
                "avatar_data": avatar_data,
                "context_data": context_data
            }, categoria="drivers_mentais")
            
            # Analisa avatar para identificar drivers ideais
            ideal_drivers = self._identify_ideal_drivers(avatar_data, context_data)
            
            # Gera drivers customizados
            customized_drivers = self._generate_customized_drivers(ideal_drivers, avatar_data, context_data)
            
            if not customized_drivers:
                logger.error("❌ Falha na geração de drivers customizados")
                # Usa fallback em vez de falhar
                logger.warning("🔄 Usando drivers básicos como fallback")
                customized_drivers = self._generate_fallback_drivers_system(context_data)
            
            # Salva drivers customizados
            salvar_etapa("drivers_customizados", customized_drivers, categoria="drivers_mentais")
            
            # Cria roteiros de ativação
            activation_scripts = self._create_activation_scripts(customized_drivers, avatar_data)
            
            # Gera frases de ancoragem
            anchor_phrases = self._generate_anchor_phrases(customized_drivers, avatar_data)
            
            result = {
                'drivers_customizados': customized_drivers,
                'roteiros_ativacao': activation_scripts,
                'frases_ancoragem': anchor_phrases,
                'drivers_universais_utilizados': [d['nome'] for d in ideal_drivers],
                'personalizacao_nivel': self._calculate_personalization_level(customized_drivers),
                'validation_status': 'VALID',
                'generation_timestamp': time.time()
            }
            
            # Salva resultado final imediatamente
            salvar_etapa("drivers_final", result, categoria="drivers_mentais")
            
            logger.info("✅ Drivers mentais customizados gerados com sucesso")
            return result
            
        except Exception as e:
            logger.error(f"❌ Erro ao gerar drivers mentais: {str(e)}")
            salvar_erro("drivers_sistema", e, contexto={"segmento": context_data.get('segmento')})
            
            # Fallback para sistema básico em caso de erro
            logger.warning("🔄 Gerando drivers básicos como fallback...")
            return self._generate_fallback_drivers_system(context_data)
    
    def _identify_ideal_drivers(self, avatar_data: Dict[str, Any], context_data: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Identifica drivers ideais baseado no avatar e contexto expandido"""
        
        ideal_drivers = []
        
        # Analisa dores para identificar drivers primários
        dores = avatar_data.get('dores_viscerais', [])
        desejos = avatar_data.get('desejos_ocultos', [])
        objecoes = avatar_data.get('objecoes_principais', [])
        
        # DRIVERS EMOCIONAIS PRIMÁRIOS baseados em dores
        if any(word in ' '.join(dores).lower() for word in ['tempo', 'pressa', 'urgente', 'prazo']):
            ideal_drivers.append(self.universal_drivers['relogio_psicologico'])
        
        if any(word in ' '.join(dores).lower() for word in ['sozinho', 'perdido', 'confuso', 'orientação']):
            ideal_drivers.append(self.universal_drivers['mentor_salvador'])
        
        if any(word in ' '.join(dores).lower() for word in ['fracasso', 'tentativa', 'erro', 'frustração']):
            ideal_drivers.append(self.universal_drivers['ferida_exposta'])
        
        if any(word in ' '.join(dores).lower() for word in ['ambiente', 'pessoas', 'círculo', 'negativo']):
            ideal_drivers.append(self.universal_drivers['ambiente_vampiro'])
        
        if any(word in ' '.join(dores).lower() for word in ['resultado', 'estagnado', 'parado', 'mesmo']):
            ideal_drivers.append(self.universal_drivers['diagnostico_brutal'])
        
        # DRIVERS RACIONAIS baseados em objeções
        if any(word in ' '.join(objecoes).lower() for word in ['dinheiro', 'caro', 'investimento', 'preço']):
            ideal_drivers.append(self.universal_drivers['custo_invisivel'])
        
        if any(word in ' '.join(objecoes).lower() for word in ['sozinho', 'consegue', 'tentativa', 'método']):
            ideal_drivers.append(self.universal_drivers['metodo_vs_sorte'])
        
        if any(word in ' '.join(objecoes).lower() for word in ['confiança', 'prova', 'funciona', 'verdade']):
            ideal_drivers.append(self.universal_drivers['prova_matematica'])
        
        # DRIVERS DE DESEJO baseados em aspirações
        if any(word in ' '.join(desejos).lower() for word in ['reconhecimento', 'autoridade', 'expert', 'referência']):
            ideal_drivers.append(self.universal_drivers['identidade_aprisionada'])
        
        if any(word in ' '.join(desejos).lower() for word in ['liberdade', 'automação', 'sistema', 'escalável']):
            ideal_drivers.append(self.universal_drivers['atalho_etico'])
        
        # DRIVERS UNIVERSAIS SEMPRE IMPORTANTES
        essential_drivers = [
            'ambicao_expandida',
            'decisao_binaria', 
            'oportunidade_oculta',
            'coragem_necessaria'
        ]
        
        for driver_key in essential_drivers:
            if driver_key in self.universal_drivers:
                ideal_drivers.append(self.universal_drivers[driver_key])
        
        # Remove duplicatas mantendo ordem
        seen = set()
        unique_drivers = []
        for driver in ideal_drivers:
            driver_id = driver.get('nome', '')
            if driver_id not in seen:
                seen.add(driver_id)
                unique_drivers.append(driver)
        
        return unique_drivers[:12]  # Máximo 12 drivers para o algoritmo
    
    def _generate_customized_drivers(
        self, 
        ideal_drivers: List[Dict[str, Any]], 
        avatar_data: Dict[str, Any], 
        context_data: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """Gera arsenal massivo de drivers customizados usando IA"""
        
        try:
            segmento = context_data.get('segmento', 'negócios')
            produto = context_data.get('produto', 'produto/serviço')
            
            # PROMPT MASSIVO PARA 19+ DRIVERS
            prompt = f"""
Você é o ARQUITETO SUPREMO DE DRIVERS MENTAIS. Crie um ARSENAL MASSIVO de 15-20 drivers mentais customizados para {segmento}.

CONTEXTO CRÍTICO:
- Segmento: {segmento}
- Produto: {produto}
- Avatar: {json.dumps(avatar_data, indent=2, ensure_ascii=False)[:1500]}

OS 19 DRIVERS UNIVERSAIS COMO BASE:
{json.dumps(list(self.universal_drivers.keys()), indent=2, ensure_ascii=False)}

INSTRUÇÕES BRUTAIS:
1. Crie MÍNIMO 15 drivers, MÁXIMO 20
2. Use os 19 universais como base mas CUSTOMIZE TUDO
3. Cada driver deve ser ÚNICO, VISCERAL e ESPECÍFICO para {segmento}
4. Inclua drivers emocionais primários E racionais complementares
5. Foque nas dores mais profundas do avatar
6. Histórias devem ter 200+ palavras e ser ESPECÍFICAS
7. Frases de ancoragem devem ser MEMORÁVEIS
8. Cada driver deve atacar uma objeção ou instalar uma crença

RETORNE APENAS JSON VÁLIDO:

```json
[
  {{
    "nome": "Nome Impactante (máx 3 palavras)",
    "gatilho_central": "Emoção ou lógica core específica",
    "definicao_visceral": "1-2 frases que capturam essência",
    "mecanica_psicologica": "Como funciona no cérebro",
    "categoria": "emocional_primario|racional_complementar",
    "momento_instalacao": "Quando plantar durante jornada",
    "roteiro_ativacao": {{
      "pergunta_abertura": "Pergunta que expõe ferida específica",
      "historia_analogia": "História DETALHADA de 200+ palavras específica para {segmento}",
      "metafora_visual": "Metáfora visual poderosa e memorável",
      "comando_acao": "Comando específico que direciona comportamento"
    }},
    "frases_ancoragem": [
      "Frase 1 memorável e repetível",
      "Frase 2 que reativa o driver",
      "Frase 3 que intensifica tensão",
      "Frase 4 que ancora na memória",
      "Frase 5 que força ação"
    ],
    "prova_logica": "Dados/fatos específicos que sustentam",
    "loop_reforco": "Como reativar em momentos posteriores",
    "objecao_destruida": "Que objeção específica este driver neutraliza",
    "nivel_intensidade": "baixa|media|alta|maxima"
  }}
]
```

COMECE GERANDO O ARSENAL COMPLETO AGORA!
"""
            
            response = ai_manager.generate_analysis(prompt, max_tokens=4000)
            
            if response:
                clean_response = response.strip()
                if "```json" in clean_response:
                    start = clean_response.find("```json") + 7
                    end = clean_response.rfind("```")
                    clean_response = clean_response[start:end].strip()
                
                try:
                    drivers = json.loads(clean_response)
                    if isinstance(drivers, list) and len(drivers) >= 10:
                        logger.info(f"✅ Arsenal de {len(drivers)} drivers customizados gerado com IA")
                        return drivers
                    else:
                        logger.warning(f"⚠️ IA retornou apenas {len(drivers) if isinstance(drivers, list) else 0} drivers")
                except json.JSONDecodeError as e:
                    logger.warning(f"⚠️ IA retornou JSON inválido: {str(e)}")
            
            # Fallback para arsenal expandido
            return self._create_expanded_drivers_arsenal(context_data)
            
        except Exception as e:
            logger.error(f"❌ Erro ao gerar arsenal de drivers: {str(e)}")
            return self._create_expanded_drivers_arsenal(context_data)
    
    def _create_expanded_drivers_arsenal(self, context_data: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Cria arsenal expandido de drivers como fallback robusto"""
        
        segmento = context_data.get('segmento', 'negócios')
        produto = context_data.get('produto', 'solução')
        
        return [
            # DRIVERS EMOCIONAIS PRIMÁRIOS
            {
                'nome': 'Ferida Exposta',
                'gatilho_central': f'Dor não resolvida em {segmento}',
                'definicao_visceral': f'Trazer à consciência problemas reprimidos de {segmento}',
                'mecanica_psicologica': 'Ativa sistema límbico de alerta',
                'categoria': 'emocional_primario',
                'roteiro_ativacao': {
                    'pergunta_abertura': f'Você ainda está lutando com {segmento} mesmo sabendo que está perdendo tempo e dinheiro?',
                    'historia_analogia': f'Conheci um profissional de {segmento} que fingiu por 2 anos que estava tudo bem. Trabalhava dobrado, dormia mal, brigava em casa. Quando finalmente admitiu que precisava de ajuda, descobriu que o problema não era falta de esforço, era falta de estratégia. Em 90 dias reorganizou tudo e recuperou sua vida pessoal.',
                    'metafora_visual': f'É como ter uma infecção e fingir que é só um arranhão. Quanto mais ignora, mais spread.',
                    'comando_acao': f'Pare de fingir que está tudo bem em {segmento} e encare a realidade'
                },
                'frases_ancoragem': [
                    f'Problemas ignorados em {segmento} não desaparecem, se multiplicam',
                    'Admitir o problema é o primeiro passo para a solução',
                    'Fingir que está tudo bem é o caminho para o colapso'
                ],
                'prova_logica': f'85% dos fracassos em {segmento} começam com negação da realidade',
                'objecao_destruida': 'Minimização de problemas',
                'nivel_intensidade': 'alta'
            },
            {
                'nome': 'Relógio Psicológico',
                'gatilho_central': 'Urgência temporal existencial',
                'definicao_visceral': 'Cada momento perdido é oportunidade que não volta',
                'mecanica_psicologica': 'Ativa cortisol de urgência temporal',
                'categoria': 'emocional_primario',
                'roteiro_ativacao': {
                    'pergunta_abertura': f'Quantos anos você ainda vai desperdiçar tentando resolver {segmento} sozinho?',
                    'historia_analogia': f'Tem um cara que conheço, inteligente, esforçado, sempre "planejando" entrar sério em {segmento}. 2018: "Ano que vem eu foco nisso". 2019: "Agora não dá, tenho outras prioridades". 2020: pandemia atrapalhou. 2021: "ainda não é o momento". 2024: ainda na mesma. Agora olha pros mais novos que começaram depois dele e já passaram na frente. O tempo não perdoa procrastinação.',
                    'metafora_visual': 'É como um trem que passa na sua estação uma vez por ano. Você fica sempre "se preparando" para o próximo, mas nunca sobe.',
                    'comando_acao': f'Suba no trem de {segmento} AGORA ou aceite ficar para trás'
                },
                'frases_ancoragem': [
                    'Tempo perdido nunca volta',
                    'Enquanto você planeja, outros executam',
                    'Procrastinação é o assassino silencioso dos sonhos',
                    'Cada dia adiado é um dia que seus concorrentes ganham vantagem'
                ],
                'prova_logica': 'Profissionais que agem imediatamente têm 340% mais chances de sucesso',
                'objecao_destruida': 'Procrastinação e "não é o momento"',
                'nivel_intensidade': 'maxima'
            },
            {
                'nome': 'Diagnóstico Brutal',
                'gatilho_central': 'Confronto implacável com realidade',
                'definicao_visceral': 'Destruir ilusões confortáveis com fatos cruéis',
                'mecanica_psicologica': 'Quebra negação através de evidência irrefutável',
                'categoria': 'emocional_primario',
                'roteiro_ativacao': {
                    'pergunta_abertura': f'Você tem coragem de ver seus números reais em {segmento}?',
                    'historia_analogia': f'Atendi um empresário que insistia que estava "indo bem" em {segmento}. Quando fizemos a análise real: 60% dos leads perdidos por falta de follow-up, 30% de margem jogada fora por desorganização, 40h semanais desperdiçadas em tarefas que poderiam ser automatizadas. R$ 50 mil por mês vazando por furos básicos. Quando viu os números na tela, quebrou. "Como eu fui cego por tanto tempo?" Mas só depois de aceitar a realidade brutal conseguiu consertar.',
                    'metafora_visual': 'É como estar numa casa pegando fogo e insistir que é só o aquecedor ligado.',
                    'comando_acao': f'Encare seus números reais em {segmento} e pare de se iludir'
                },
                'frases_ancoragem': [
                    'Números não mentem, pessoas sim',
                    'Autoengano é o luxo mais caro que existe',
                    'A verdade dói, mas a ilusão mata',
                    'Realidade ignorada se torna tragédia anunciada'
                ],
                'prova_logica': '73% das pessoas superestimam sua performance real em 200%',
                'objecao_destruida': 'Autoengano e minimização de problemas',
                'nivel_intensidade': 'maxima'
            },
            {
                'nome': 'Ambiente Vampiro',
                'gatilho_central': 'Consciência de energia sendo sugada',
                'definicao_visceral': 'Revelar como ambiente atual drena potencial',
                'mecanica_psicologica': 'Identifica drenos externos de energia vital',
                'categoria': 'emocional_primario',
                'roteiro_ativacao': {
                    'pergunta_abertura': f'Quantas pessoas ao seu redor realmente querem seu sucesso em {segmento}?',
                    'historia_analogia': f'Cliente meu vivia cercado de "amigos" que sempre tinham uma desculpa para desencorajar. "Não é o momento", "muito arriscado", "você já está bem". Quando começou a crescer em {segmento}, virou alvo de ironia sutil, comentários ácidos disfarçados de "preocupação". Percebeu que estava num círculo de medíocres que se sentia ameaçado pelo seu sucesso. Mudou de círculo social, cortou vampiros energéticos, se cercou de gente que puxa para cima. Resultado: crescimento exponencial em 6 meses.',
                    'metafora_visual': 'É como tentar subir numa escada rolante que está descendo. Por mais que você corra, o ambiente te puxa para baixo.',
                    'comando_acao': f'Corte vampiros energéticos e cerque-se de quem apoia seu crescimento em {segmento}'
                },
                'frases_ancoragem': [
                    'Você é a média das 5 pessoas com quem mais convive',
                    'Ambiente medíocre produz resultados medíocres',
                    'Vampiros energéticos sugam seu potencial',
                    'Mude o ambiente ou ele mudará você'
                ],
                'prova_logica': 'Pessoas em ambientes de alta performance têm 5x mais chance de sucesso',
                'objecao_destruida': 'Influências negativas do círculo social',
                'nivel_intensidade': 'alta'
            },
            {
                'nome': 'Método vs Sorte',
                'gatilho_central': 'Sistema estruturado vs tentativa aleatória',
                'definicao_visceral': 'Contrastar caos da improvisação com poder do método',
                'mecanica_psicologica': 'Ativa preferência neurológica por ordem',
                'categoria': 'racional_complementar',
                'roteiro_ativacao': {
                    'pergunta_abertura': f'Você está tentando "dar um jeito" em {segmento} ou seguindo um método comprovado?',
                    'historia_analogia': f'Dois caras começaram no mesmo dia em {segmento}. João ficou "tentando", seguindo dicas aleatórias do YouTube, mudando estratégia a cada semana, reinventando a roda. Pedro seguiu um método estruturado, passo a passo, mesmo quando parecia "lento". Depois de 1 ano: João ainda estava quebrando a cabeça com problemas básicos, Pedro já era referência no mercado. A diferença? João cortava mato com foice, Pedro pegou a autoestrada.',
                    'metafora_visual': 'Tentar sem método é como cozinhar sem receita. Pode dar certo... ou virar desastre.',
                    'comando_acao': f'Pare de improvisar em {segmento} e siga um método comprovado'
                },
                'frases_ancoragem': [
                    'Método elimina tentativa e erro',
                    'Improviso é luxo para quem já domina o básico',
                    'Sistema funciona mesmo quando você não está funcionando',
                    'Sorte é para quem não tem método'
                ],
                'prova_logica': 'Metodologia reduz tempo para resultado em 75%',
                'objecao_destruida': 'Tentativa de fazer sozinho sem estrutura',
                'nivel_intensidade': 'media'
            },
            {
                'nome': 'Decisão Binária',
                'gatilho_central': 'Eliminação radical de zona cinzenta',
                'definicao_visceral': 'Forçar escolha entre duas únicas opções',
                'mecanica_psicologica': 'Força circuito de decisão através de simplicidade',
                'categoria': 'racional_complementar',
                'roteiro_ativacao': {
                    'pergunta_abertura': f'Você vai dominar {segmento} nos próximos 6 meses ou vai aceitar ficar na mediocridade para sempre?',
                    'historia_analogia': f'Cliente chegou pra mim totalmente perdido em {segmento}. Milhões de "talvez", "possivelmente", "vou pensar". Coloquei na parede: "Ou você decide HOJE que vai ser um expert em {segmento} ou aceita que vai ser medíocre para sempre. Não existe meio termo." Silêncio de 30 segundos. "Quero ser expert." Pronto. Decisão tomada. 8 meses depois estava dando consultoria para grandes empresas.',
                    'metafora_visual': 'É como estar na borda de um abismo. Ou você pula para o outro lado ou volta. Ficar na borda não é opção.',
                    'comando_acao': f'DECIDA AGORA: expert em {segmento} ou medíocre para sempre'
                },
                'frases_ancoragem': [
                    'Não existem meio-termos para o sucesso',
                    'Indecisão é decisão de fracassar',
                    'Ou você escolhe ou a vida escolhe por você',
                    'Zona cinzenta é zona de derrota'
                ],
                'prova_logica': 'Pessoas que tomam decisões binárias têm 60% mais chance de sucesso',
                'objecao_destruida': 'Indecisão e procrastinação',
                'nivel_intensidade': 'maxima'
            }
            # ... mais drivers serão adicionados automaticamente
        ]
    
    def _create_activation_scripts(self, drivers: List[Dict[str, Any]], avatar_data: Dict[str, Any]) -> Dict[str, Any]:
        """Cria roteiros de ativação para cada driver"""
        
        scripts = {}
        
        for driver in drivers:
            driver_name = driver.get('nome', 'Driver')
            roteiro = driver.get('roteiro_ativacao', {})
            
            scripts[driver_name] = {
                'abertura': roteiro.get('pergunta_abertura', ''),
                'desenvolvimento': roteiro.get('historia_analogia', ''),
                'fechamento': roteiro.get('comando_acao', ''),
                'tempo_estimado': '3-5 minutos',
                'intensidade': 'Alta'
            }
        
        return scripts
    
    def _generate_anchor_phrases(self, drivers: List[Dict[str, Any]], avatar_data: Dict[str, Any]) -> Dict[str, List[str]]:
        """Gera frases de ancoragem para cada driver"""
        
        anchor_phrases = {}
        
        for driver in drivers:
            driver_name = driver.get('nome', 'Driver')
            frases = driver.get('frases_ancoragem', [])
            
            if frases:
                anchor_phrases[driver_name] = frases
            else:
                # Frases padrão
                anchor_phrases[driver_name] = [
                    f"Este é o momento de ativar {driver_name}",
                    f"Você sente o impacto de {driver_name}",
                    f"Agora {driver_name} faz sentido para você"
                ]
        
        return anchor_phrases
    
    def _calculate_personalization_level(self, drivers: List[Dict[str, Any]]) -> str:
        """Calcula nível de personalização dos drivers"""
        
        if not drivers:
            return "Baixo"
        
        # Verifica se tem histórias específicas
        has_stories = sum(1 for d in drivers if len(d.get('roteiro_ativacao', {}).get('historia_analogia', '')) > 100)
        
        # Verifica se tem frases de ancoragem
        has_anchors = sum(1 for d in drivers if len(d.get('frases_ancoragem', [])) >= 3)
        
        personalization_score = (has_stories + has_anchors) / (len(drivers) * 2)
        
        if personalization_score >= 0.8:
            return "Alto"
        elif personalization_score >= 0.5:
            return "Médio"
        else:
            return "Baixo"
    
    def _create_basic_avatar(self, context_data: Dict[str, Any]) -> Dict[str, Any]:
        """Cria avatar básico quando não há dados disponíveis"""
        
        segmento = context_data.get('segmento', 'negócios')
        produto = context_data.get('produto', 'produto/serviço')
        
        return {
            'dores_viscerais': [
                f"Dificuldade para se destacar no mercado de {segmento}",
                f"Falta de estratégia clara para {produto}",
                "Resultados inconsistentes e imprevisíveis",
                "Concorrência acirrada e diferenciação difícil",
                "Falta de autoridade no mercado"
            ],
            'desejos_ocultos': [
                f"Ser reconhecido como autoridade em {segmento}",
                "Ter liberdade financeira e temporal",
                "Impactar positivamente a vida das pessoas",
                "Construir um legado duradouro",
                "Ter clientes disputando para trabalhar comigo"
            ],
            'objecoes_principais': [
                "Não tenho tempo suficiente",
                "O investimento é alto demais",
                "Meu caso é específico demais",
                "Já tentei outras coisas sem sucesso",
                "Preciso de mais garantias"
            ],
            'feridas_abertas_inconfessaveis': [
                f"Sente que está desperdiçando potencial em {segmento}",
                "Tem medo de nunca conseguir se destacar realmente",
                "Sente inveja dos concorrentes que têm sucesso",
                "Tem vergonha dos resultados atuais"
            ],
            'sonhos_proibidos_ardentes': [
                f"Dominar completamente o mercado de {segmento}",
                "Ter clientes disputando para trabalhar comigo",
                "Ser procurado pela mídia como especialista",
                "Ter renda passiva substancial"
            ]
        }

    def _generate_fallback_drivers_system(self, context_data: Dict[str, Any]) -> Dict[str, Any]:
        """Gera sistema de drivers básico como fallback"""
        
        segmento = context_data.get('segmento', 'negócios')
        
        fallback_drivers = self._create_expanded_drivers_arsenal(context_data)
        
        return {
            'drivers_customizados': fallback_drivers,
            'roteiros_ativacao': {
                driver['nome']: {
                    'abertura': driver['roteiro_ativacao']['pergunta_abertura'],
                    'desenvolvimento': driver['roteiro_ativacao']['historia_analogia'],
                    'fechamento': driver['roteiro_ativacao']['comando_acao'],
                    'tempo_estimado': '3-5 minutos'
                } for driver in fallback_drivers
            },
            'frases_ancoragem': {
                driver['nome']: driver['frases_ancoragem'] for driver in fallback_drivers
            },
            'validation_status': 'FALLBACK_VALID',
            'generation_timestamp': time.time(),
            'fallback_mode': True
        }

# Instância global
mental_drivers_architect = MentalDriversArchitect()