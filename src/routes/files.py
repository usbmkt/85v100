#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ARQV30 Enhanced v2.0 - Rotas para Gerenciamento de Arquivos
Sistema apenas local - SEM Supabase
"""

import os
import json
import logging
from datetime import datetime
from flask import Blueprint, request, jsonify, send_file
from services.local_file_manager import local_file_manager
# Removed: from database import db_manager

logger = logging.getLogger(__name__)

files_bp = Blueprint('files', __name__, url_prefix='/api')

@files_bp.route('/list_local_analyses', methods=['GET'])
def list_local_analyses():
    """Lista análises salvas localmente"""

    try:
        analyses = local_file_manager.list_local_analyses()

        return jsonify({
            'success': True,
            'analyses': analyses,
            'total': len(analyses),
            'timestamp': datetime.now().isoformat()
        })

    except Exception as e:
        logger.error(f"Erro ao listar análises locais: {str(e)}")
        return jsonify({
            'error': 'Erro ao listar análises locais',
            'message': str(e)
        }), 500

@files_bp.route('/get_analysis/<analysis_id>', methods=['GET'])
def get_analysis_details(analysis_id):
    """Obtém detalhes de uma análise específica"""

    try:
        # Carrega análise completa
        analysis_data = local_file_manager.load_complete_analysis(analysis_id)

        if not analysis_data:
            return jsonify({
                'error': 'Análise não encontrada',
                'analysis_id': analysis_id
            }), 404

        # Busca arquivos relacionados
        files = local_file_manager.get_analysis_files(analysis_id)

        return jsonify({
            'success': True,
            'analysis_id': analysis_id,
            'analysis_data': analysis_data,
            'files': files,
            'total_files': len(files)
        })

    except Exception as e:
        logger.error(f"Erro ao obter análise {analysis_id}: {str(e)}")
        return jsonify({
            'error': 'Erro ao obter análise',
            'message': str(e)
        }), 500

@files_bp.route('/get_analysis_section/<analysis_id>/<section_name>', methods=['GET'])
def get_analysis_section(analysis_id, section_name):
    """Carrega uma seção específica da análise"""

    try:
        section_data = local_file_manager.load_analysis_section(analysis_id, section_name)

        if not section_data:
            return jsonify({
                'error': f'Seção {section_name} não encontrada',
                'analysis_id': analysis_id,
                'section_name': section_name
            }), 404

        return jsonify({
            'success': True,
            'analysis_id': analysis_id,
            'section_name': section_name,
            'data': section_data
        })

    except Exception as e:
        logger.error(f"Erro ao carregar seção {section_name} da análise {analysis_id}: {str(e)}")
        return jsonify({
            'error': 'Erro ao carregar seção',
            'message': str(e)
        }), 500

@files_bp.route('/get_analysis_files/<analysis_id>', methods=['GET'])
def get_analysis_files(analysis_id):
    """Obtém arquivos de uma análise específica"""

    try:
        # Busca arquivos locais
        local_files = local_file_manager.get_analysis_files(analysis_id)

        return jsonify({
            'success': True,
            'analysis_id': analysis_id,
            'local_files': local_files,
            'total_files': len(local_files)
        })

    except Exception as e:
        logger.error(f"Erro ao obter arquivos da análise {analysis_id}: {str(e)}")
        return jsonify({
            'error': 'Erro ao obter arquivos da análise',
            'message': str(e)
        }), 500

@files_bp.route('/delete_analysis/<analysis_id>', methods=['DELETE'])
def delete_local_analysis(analysis_id):
    """Remove análise local por ID"""

    try:
        # Remove arquivos locais
        local_result = local_file_manager.delete_local_analysis(analysis_id)

        if local_result:
            return jsonify({
                'success': True,
                'message': 'Análise removida com sucesso',
                'analysis_id': analysis_id,
                'local_deleted': local_result
            })
        else:
            return jsonify({
                'success': False,
                'message': 'Análise não encontrada',
                'analysis_id': analysis_id
            }), 404

    except Exception as e:
        logger.error(f"Erro ao deletar análise {analysis_id}: {str(e)}")
        return jsonify({
            'error': 'Erro ao deletar análise',
            'message': str(e)
        }), 500

@files_bp.route('/get_file_content', methods=['GET'])
def get_file_content():
    """Obtém conteúdo de um arquivo específico"""

    try:
        file_path = request.args.get('file_path')

        if not file_path or not os.path.exists(file_path):
            return jsonify({
                'error': 'Arquivo não encontrado',
                'file_path': file_path
            }), 404

        # Verifica se é arquivo JSON
        if file_path.endswith('.json'):
            with open(file_path, 'r', encoding='utf-8') as f:
                content = json.load(f)

            return jsonify({
                'success': True,
                'file_path': file_path,
                'content': content,
                'file_type': 'json'
            })
        else:
            # Para outros tipos, retorna como texto
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            return jsonify({
                'success': True,
                'file_path': file_path,
                'content': content,
                'file_type': 'text'
            })

    except Exception as e:
        logger.error(f"Erro ao ler arquivo: {str(e)}")
        return jsonify({
            'error': 'Erro ao ler arquivo',
            'message': str(e)
        }), 500

@files_bp.route('/download_file', methods=['GET'])
def download_file():
    """Faz download de um arquivo específico"""

    try:
        file_path = request.args.get('file_path')

        if not file_path or not os.path.exists(file_path):
            return jsonify({
                'error': 'Arquivo não encontrado',
                'file_path': file_path
            }), 404

        return send_file(
            file_path,
            as_attachment=True,
            download_name=os.path.basename(file_path)
        )

    except Exception as e:
        logger.error(f"Erro ao fazer download do arquivo: {str(e)}")
        return jsonify({
            'error': 'Erro ao fazer download',
            'message': str(e)
        }), 500

@files_bp.route('/storage_stats', methods=['GET'])
def get_storage_stats():
    """Obtém estatísticas de armazenamento"""

    try:
        stats = local_file_manager.get_storage_stats()
        analyses = local_file_manager.list_local_analyses()

        return jsonify({
            'success': True,
            'storage_stats': stats,
            'analyses_count': len(analyses),
            'recent_analyses': analyses[:5],  # 5 mais recentes
            'timestamp': datetime.now().isoformat()
        })

    except Exception as e:
        logger.error(f"Erro ao obter estatísticas: {str(e)}")
        return jsonify({
            'error': 'Erro ao obter estatísticas',
            'message': str(e)
        }), 500

@files_bp.route('/export_analysis/<analysis_id>', methods=['GET'])
def export_analysis(analysis_id):
    """Exporta análise completa como JSON"""

    try:
        analysis_data = local_file_manager.load_complete_analysis(analysis_id)

        if not analysis_data:
            return jsonify({
                'error': 'Análise não encontrada',
                'analysis_id': analysis_id
            }), 404

        # Adiciona metadados de exportação
        export_data = {
            'export_timestamp': datetime.now().isoformat(),
            'analysis_id': analysis_id,
            'system': 'ARQV30_Enhanced_v2.0',
            'data': analysis_data
        }

        # Salva arquivo temporário de exportação
        export_filename = f"export_{analysis_id[:8]}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        export_path = os.path.join(local_file_manager.base_dir, export_filename)

        with open(export_path, 'w', encoding='utf-8') as f:
            json.dump(export_data, f, ensure_ascii=False, indent=2)

        return send_file(
            export_path,
            as_attachment=True,
            download_name=export_filename,
            mimetype='application/json'
        )

    except Exception as e:
        logger.error(f"Erro ao exportar análise {analysis_id}: {str(e)}")
        return jsonify({
            'error': 'Erro ao exportar análise',
            'message': str(e)
        }), 500

@files_bp.route('/cleanup_temp_files', methods=['POST'])
def cleanup_temp_files():
    """Remove arquivos temporários de exportação"""

    try:
        cleaned_files = 0

        for filename in os.listdir(local_file_manager.base_dir):
            if filename.startswith('export_') and filename.endswith('.json'):
                file_path = os.path.join(local_file_manager.base_dir, filename)
                try:
                    # Remove arquivos de exportação com mais de 1 hora
                    file_age = datetime.now().timestamp() - os.path.getmtime(file_path)
                    if file_age > 3600:  # 1 hora
                        os.remove(file_path)
                        cleaned_files += 1
                except Exception as e:
                    logger.warning(f"Erro ao remover arquivo temporário {filename}: {str(e)}")

        return jsonify({
            'success': True,
            'message': f'{cleaned_files} arquivos temporários removidos',
            'cleaned_files': cleaned_files
        })

    except Exception as e:
        logger.error(f"Erro na limpeza de arquivos temporários: {str(e)}")
        return jsonify({
            'error': 'Erro na limpeza',
            'message': str(e)
        }), 500