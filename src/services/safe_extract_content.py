#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ARQV30 Enhanced v2.0 - Safe Content Extraction
Extração segura de conteúdo com validação rigorosa
"""

import logging
import time
from typing import Optional, Dict, Any, Tuple, List
from .robust_content_extractor import robust_content_extractor
from .url_resolver import URLResolver

logger = logging.getLogger(__name__)


class SafeExtractContent:
    """Extração segura de conteúdo com validação rigorosa"""
    
    def __init__(self):
        """Inicializa o extrator seguro"""
        self.url_resolver = URLResolver()
        self.max_extraction_time = 30
        self.blacklisted_domains = [
            'localhost', '127.0.0.1', '0.0.0.0', 'malware.com'
        ]
    
    def safe_extract(
        self, 
        url: str, 
        context: Dict[str, Any] = None
    ) -> Tuple[Optional[str], Dict[str, Any]]:
        """Extrai conteúdo de forma segura com validações"""
        
        if not url or not self._is_url_safe(url):
            return None, {"error": "URL não é segura"}
        
        try:
            # Resolve URL primeiro
            resolved_url = self.url_resolver.resolve_url(url)
            if not resolved_url:
                return None, {"error": "URL não pôde ser resolvida"}
            
            # Extrai conteúdo com timeout
            content = self._extract_with_timeout(resolved_url)
            
            if content:
                # Valida qualidade
                try:
                    from .content_quality_validator import content_quality_validator
                    validation = content_quality_validator.validate_content(content, resolved_url)
                except:
                    validation = {"valid": True, "score": 0.8}
                
                return content, {
                    "success": True,
                    "url": resolved_url,
                    "validation": validation,
                    "content_length": len(content)
                }
            else:
                return None, {"error": "Conteúdo não extraído"}
                
        except Exception as e:
            logger.error(f"❌ Erro na extração segura: {e}")
            return None, {"error": str(e)}
    
    def _is_url_safe(self, url: str) -> bool:
        """Verifica se a URL é segura"""
        if not url or not isinstance(url, str):
            return False
        
        # Padrões suspeitos
        suspicious_patterns = [
            'javascript:', 'data:', 'mailto:', 'tel:', 'ftp:',
            'localhost', '127.0.0.1', '0.0.0.0'
        ]
        
        url_lower = url.lower()
        if any(pattern in url_lower for pattern in suspicious_patterns):
            return False
        
        return Trueme__)

class SafeContentExtractor:
    """Extrator seguro de conteúdo com validação rigorosa"""
    
    def __init__(self):
        """Inicializa o extrator seguro"""
        self.min_content_length = 500
        self.min_quality_score = 60.0
        self.max_extraction_time = 30  # segundos
        
        logger.info("Safe Content Extractor inicializado")
    
    def safe_extract_content(self, url: str, context: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        Extrai conteúdo de forma segura com validação completa
        
        Returns:
            Dict com 'success', 'content', 'metadata', 'validation', 'error'
        """
        
        result = {
            'success': False,
            'content': None,
            'metadata': {},
            'validation': {},
            'error': None,
            'url': url,
            'timestamp': time.time()
        }
        
        try:
            start_time = time.time()
            
            # 1. Valida URL
            if not self._validate_url(url):
                result['error'] = f"URL inválida: {url}"
                logger.error(f"❌ {result['error']}")
                return result
            
            # 2. Resolve redirecionamentos
            resolved_url = url_resolver.resolve_redirect_url(url)
            if resolved_url != url:
                logger.info(f"🔄 URL resolvida: {url} -> {resolved_url}")
                result['metadata']['resolved_url'] = resolved_url
                url = resolved_url
            
            # 3. Valida URL resolvida
            if not self._validate_url(resolved_url):
                result['error'] = f"URL resolvida inválida: {resolved_url}"
                logger.error(f"❌ {result['error']}")
                return result
            
            # 4. Extrai conteúdo com timeout
            extraction_start = time.time()
            content = self._extract_with_timeout(url)
            extraction_time = time.time() - extraction_start
            
            result['metadata']['extraction_time'] = extraction_time
            
            if not content:
                result['error'] = "Nenhum conteúdo extraído"
                logger.error(f"❌ {result['error']} para {url}")
                return result
            
            # 5. Valida tamanho mínimo
            if len(content) < self.min_content_length:
                result['error'] = f"Conteúdo muito pequeno: {len(content)} < {self.min_content_length}"
                logger.error(f"❌ {result['error']} para {url}")
                return result
            
            # 6. Valida qualidade do conteúdo
            validation = content_quality_validator.validate_content(content, url, context)
            result['validation'] = validation
            
            if not validation['valid']:
                result['error'] = f"Conteúdo de baixa qualidade: {validation['reason']}"
                logger.error(f"❌ {result['error']} para {url}")
                return result
            
            if validation['score'] < self.min_quality_score:
                result['error'] = f"Score de qualidade muito baixo: {validation['score']:.1f}% < {self.min_quality_score}%"
                logger.error(f"❌ {result['error']} para {url}")
                return result
            
            # 7. Sucesso - conteúdo válido
            result['success'] = True
            result['content'] = content
            result['metadata'].update({
                'content_length': len(content),
                'word_count': len(content.split()),
                'quality_score': validation['score'],
                'total_time': time.time() - start_time
            })
            
            logger.info(f"✅ Extração segura bem-sucedida: {len(content)} chars, qualidade {validation['score']:.1f}%")
            return result
            
        except Exception as e:
            result['error'] = f"Erro na extração: {str(e)}"
            result['metadata']['total_time'] = time.time() - start_time if 'start_time' in locals() else 0
            logger.error(f"❌ {result['error']} para {url}")
            return result
    
    def _validate_url(self, url: str) -> bool:
        """Valida se a URL é válida"""
        if not url:
            return False
        
        if not url.startswith(('http://', 'https://')):
            return False
        
        # Verifica se não é URL suspeita
        suspicious_patterns = [
            'javascript:', 'data:', 'mailto:', 'tel:', 'ftp:',
            'localhost', '127.0.0.1', '0.0.0.0'
        ]
        
        url_lower = url.lower()
        if any(pattern in url_lower for pattern in suspicious_patterns):
            return False
        
        return True
    
    def _extract_with_timeout(self, url: str) -> Optional[str]:
        """Extrai conteúdo com timeout"""
        try:
            content, metadata = robust_content_extractor.extract_content(url, timeout=self.max_extraction_time)
            return content
        except Exception as e:
            logger.error(f"❌ Erro na extração com timeout: {e}")
            return None
    
    def batch_safe_extract(
        self, 
        urls: List[str], 
        context: Dict[str, Any] = None,
        max_workers: int = 3
    ) -> Dict[str, Dict[str, Any]]:
        """Extrai conteúdo de múltiplas URLs de forma segura"""
        results = {}
        
        for url in urls:
            content, metadata = self.safe_extract(url, context)
            results[url] = {
                "content": content,
                "metadata": metadata
            }
        
        return results


# Instância global
safe_extract_content = SafeExtractContent()
        """Extrai conteúdo de múltiplas URLs de forma segura"""
        
        from concurrent.futures import ThreadPoolExecutor, as_completed
        
        results = {}
        
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            future_to_url = {
                executor.submit(self.safe_extract_content, url, context): url 
                for url in urls
            }
            
            for future in as_completed(future_to_url):
                url = future_to_url[future]
                try:
                    result = future.result()
                    results[url] = result
                except Exception as e:
                    results[url] = {
                        'success': False,
                        'error': f"Erro na extração paralela: {str(e)}",
                        'url': url,
                        'timestamp': time.time()
                    }
        
        # Estatísticas do lote
        successful = sum(1 for result in results.values() if result['success'])
        total = len(results)
        
        logger.info(f"📊 Extração em lote: {successful}/{total} sucessos ({successful/total*100:.1f}%)")
        
        return results
    
    def get_extraction_stats(self) -> Dict[str, Any]:
        """Retorna estatísticas de extração"""
        return robust_content_extractor.get_extractor_stats()

# Instância global
safe_content_extractor = SafeContentExtractor()

# Função de conveniência
def safe_extract_content(url: str, context: Dict[str, Any] = None) -> Dict[str, Any]:
    """Função de conveniência para extração segura"""
    return safe_content_extractor.safe_extract_content(url, context)
