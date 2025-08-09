
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ARQV30 Enhanced v2.0 ULTRA-ROBUSTO
Sistema de Análise Ultra-Detalhada - APENAS ARQUIVOS LOCAIS
"""

import os
import sys
import socket
import logging
from datetime import datetime

# Adiciona o diretório src ao path
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))

from flask import Flask, render_template, jsonify
from flask_cors import CORS

# Configuração de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('arqv30_enhanced.log', encoding='utf-8'),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger(__name__)

def create_app():
    """Factory function para criar a aplicação Flask"""
    
    print("🚀 ARQV30 Enhanced v2.0 - Iniciando aplicação...")
    
    # Carrega variáveis de ambiente
    from services.environment_loader import load_environment
    load_environment()
    
    # Inicializa Flask
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'arqv30-ultra-secret-key-2025')
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size
    
    # CORS
    CORS(app, resources={
        r"/api/*": {
            "origins": ["http://localhost:*", "http://127.0.0.1:*", "http://0.0.0.0:*"],
            "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
            "allow_headers": ["Content-Type", "Authorization"]
        }
    })
    
    # Inicializa serviços principais
    try:
        from services.ai_manager import ai_manager
        from services.production_search_manager import production_search_manager
        from services.auto_save_manager import auto_save_manager
        
        # Inicializa componentes de análise  
        from services.enhanced_ui_manager import enhanced_ui_manager
        from services.context_intelligence_engine import context_intelligence_engine
        from services.professional_report_manager import professional_report_manager
        
        logger.info("✅ Todos os serviços principais inicializados")
        
    except Exception as e:
        logger.error(f"❌ Erro ao inicializar serviços: {str(e)}")
        raise
    
    # Registra rotas principais
    @app.route('/')
    def index():
        """Página principal"""
        return render_template('enhanced_interface.html')
    
    @app.route('/api/app_status')
    def app_status():
        """Status da aplicação"""
        try:
            return jsonify({
                'status': 'running',
                'version': '2.0-ULTRA-ROBUSTO',
                'timestamp': datetime.now().isoformat(),
                'database_connected': False,
                'storage_type': 'local_files_only',
                'ai_providers': ['gemini', 'openai', 'groq', 'huggingface'],
                'search_providers': ['websailor', 'google', 'exa', 'serper', 'tavily']
            })
        except Exception as e:
            logger.error(f"Erro no status: {str(e)}")
            return jsonify({
                'status': 'error',
                'message': str(e)
            }), 500
    
    @app.route('/api/get_agent_capabilities')
    def get_agent_capabilities():
        """Capacidades dos agentes"""
        return jsonify({
            'success': True,
            'capabilities': {
                'archaeological_master': {
                    'description': 'Análise arqueológica de mercado',
                    'status': 'active'
                },
                'visceral_master': {
                    'description': 'Persuasão visceral e copywriting',
                    'status': 'active'
                },
                'visual_proofs_director': {
                    'description': 'Diretor de provas visuais',
                    'status': 'active'
                },
                'mental_drivers_architect': {
                    'description': 'Arquiteto de drivers mentais',
                    'status': 'active'
                },
                'anti_objection_system': {
                    'description': 'Sistema anti-objeção',
                    'status': 'active'
                },
                'future_prediction_engine': {
                    'description': 'Engine de predições futuras',
                    'status': 'active'
                }
            }
        })
    
    # Registra blueprints
    try:
        from routes.analysis import analysis_bp
        from routes.enhanced_analysis import enhanced_analysis_bp
        from routes.progress import progress_bp
        from routes.user import user_bp
        from routes.files import files_bp
        from routes.pdf_generator import pdf_bp
        from routes.monitoring import monitoring_bp
        from routes.forensic_analysis import forensic_bp
        from routes.mcp import mcp_bp
        
        app.register_blueprint(analysis_bp)
        app.register_blueprint(enhanced_analysis_bp)
        app.register_blueprint(progress_bp)
        app.register_blueprint(user_bp)
        app.register_blueprint(files_bp)
        app.register_blueprint(pdf_bp)
        app.register_blueprint(monitoring_bp)
        app.register_blueprint(forensic_bp)
        app.register_blueprint(mcp_bp)
        
        logger.info("✅ Todas as rotas registradas")
        
    except Exception as e:
        logger.error(f"❌ Erro ao registrar rotas: {str(e)}")
        raise
    
    # Error handlers
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({'error': 'Endpoint não encontrado'}), 404
    
    @app.errorhandler(500)
    def internal_error(error):
        logger.error(f"Erro interno: {str(error)}")
        return jsonify({'error': 'Erro interno do servidor'}), 500
    
    return app

def find_free_port(start_port=5000, max_attempts=10):
    """Encontra uma porta livre"""
    for port in range(start_port, start_port + max_attempts):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind(('0.0.0.0', port))
                return port
        except OSError:
            continue
    return None

def main():
    """Função principal"""
    try:
        app = create_app()
        
        # Encontra porta disponível
        port = find_free_port()
        if not port:
            logger.error("❌ Não foi possível encontrar uma porta disponível")
            sys.exit(1)
        
        if port != 5000:
            logger.warning(f"⚠️ Porta 5000 ocupada, usando porta {port}")
        
        # Informações do servidor
        print("\n" + "="*60)
        print(f"🌐 Servidor: http://0.0.0.0:{port}")
        print("🔧 Modo: Desenvolvimento")
        print("📊 Interface: Análise Ultra-Detalhada de Mercado")
        print("🤖 IA: Gemini 2.5 Pro + Groq + Fallbacks")
        print("🔍 Pesquisa: WebSailor + Google + Múltiplos Engines")
        print("💾 Banco: APENAS ARQUIVOS LOCAIS")
        print("🛡️ Sistema: Ultra-Robusto com Salvamento Automático")
        print("")
        print("✅ RECURSOS ATIVADOS:")
        print("- Análise com múltiplas IAs")
        print("- Pesquisa web profunda")
        print("- Processamento de anexos inteligente")
        print("- Geração de relatórios PDF")
        print("- Avatar ultra-detalhado")
        print("- Drivers mentais customizados")
        print("- Análise de concorrência profunda")
        print("")
        print("="*60)
        print("✅ ARQV30 Enhanced v2.0 PRONTO!")
        print("="*60)
        print("Pressione Ctrl+C para parar o servidor")
        print("="*60)
        
        # Inicia o servidor
        app.run(
            host='0.0.0.0',
            port=port,
            debug=True,
            threaded=True
        )
        
    except KeyboardInterrupt:
        print("\n🛑 Servidor interrompido pelo usuário")
    except Exception as e:
        logger.error(f"❌ Erro fatal: {str(e)}")
        sys.exit(1)

if __name__ == '__main__':
    main()
