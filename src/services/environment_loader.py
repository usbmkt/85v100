
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ARQV30 Enhanced v2.0 - Environment Loader
Carregador robusto de variáveis de ambiente com validação
"""

import os
import logging
from pathlib import Path
from dotenv import load_dotenv
from typing import Dict, Any, Optional

logger = logging.getLogger(__name__)

class EnvironmentLoader:
    """Carregador robusto de variáveis de ambiente"""

    def __init__(self):
        """Inicializa o carregador de ambiente"""
        self.env_loaded = False
        self.missing_vars = []
        self.load_environment()

    def load_environment(self):
        """Carrega variáveis de ambiente do arquivo .env"""
        try:
            # Procura arquivo .env no diretório atual e pai
            env_paths = ['.env', '../.env', '../../.env']
            env_file = None

            for path in env_paths:
                if os.path.exists(path):
                    env_file = path
                    break

            if env_file:
                load_dotenv(env_file)
                logger.info(f"✅ Arquivo .env carregado: {env_file}")

                # Verifica variáveis críticas
                self.validate_critical_vars()

                # Define valores padrão se necessário
                self._set_default_values()

                logger.info("✅ Todas as variáveis críticas configuradas")
                return True
            else:
                logger.warning("⚠️ Arquivo .env não encontrado")
                return False

        except Exception as e:
            logger.error(f"❌ Erro ao carregar ambiente: {e}")
            return False

    def _set_default_values(self):
        """Define valores padrão para variáveis de ambiente"""
        defaults = {
            'FLASK_ENV': 'development',
            'HOST': '0.0.0.0',
            'PORT': '5000',
            'CORS_ORIGINS': '*',
            'LOG_LEVEL': 'INFO',
            'CACHE_ENABLED': 'true',
            'SEARCH_CACHE_ENABLED': 'true',
            'SEARCH_CACHE_TTL': '3600',
            'RATE_LIMIT_ENABLED': 'true',
            'SECURE_HEADERS_ENABLED': 'true',
            'GZIP_ENABLED': 'true'
        }

        for key, value in defaults.items():
            if not os.getenv(key):
                os.environ[key] = value

    def validate_critical_vars(self):
        """Valida variáveis críticas e configura valores padrão"""

        # Variáveis obrigatórias (apenas locais)
        required_vars = {
            'GEMINI_API_KEY': 'AIzaSyCERwa-oIFWewEpuAZt1mxxmm4A3sQo9Es'
        }

        # Variáveis recomendadas
        recommended_vars = {
            'GROQ_API_KEY': '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',
            'GOOGLE_SEARCH_KEY': 'AIzaSyDwIFvCvailaG6B7xtysujm0djJn1zlx18',
            'GOOGLE_CSE_ID': 'c207a51dd04f9488a',
            'MCP_SEQUENTIAL_THINKING_URL': 'https://smithery.ai/server/@xinzhongyouhai/mcp-sequentialthinking-tools',
            'MCP_SUPADATA_URL': 'https://smithery.ai/server/@supadata-ai/mcp'
        }

        # Configura variáveis obrigatórias se não estiverem definidas
        for var_name, default_value in required_vars.items():
            if not os.getenv(var_name):
                os.environ[var_name] = default_value
                logger.info(f"✅ {var_name} configurado")

        # Configura variáveis recomendadas se não estiverem definidas
        for var_name, default_value in recommended_vars.items():
            if not os.getenv(var_name):
                os.environ[var_name] = default_value
                logger.info(f"✅ {var_name} configurado")

        # Verifica se ainda há variáveis ausentes
        self.missing_vars = []
        for var_name in required_vars.keys():
            if not os.getenv(var_name):
                self.missing_vars.append(var_name)

        if self.missing_vars:
            logger.error(f"❌ Variáveis críticas ausentes: {', '.join(self.missing_vars)}")
            self.env_loaded = False
        else:
            logger.info("✅ Todas as variáveis críticas configuradas")
            self.env_loaded = True

    def validate_environment(self) -> Dict[str, Any]:
        """Valida o ambiente e retorna status"""
        return {
            'valid': self.env_loaded,
            'missing': self.missing_vars
        }

# Instância global
environment_loader = EnvironmentLoader()

# Função de conveniência
def ensure_environment_loaded():
    """Garante que o ambiente foi carregado"""
    if not environment_loader.env_loaded:
        environment_loader.load_environment()
    return environment_loader.env_loaded

def load_environment():
    """Função para carregar ambiente - compatibilidade"""
    return environment_loader.load_environment()
