
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ARQV30 Enhanced v2.0 - URL Resolver
Resolve e limpa URLs problemáticas
"""

import logging
import re
from urllib.parse import urlparse, unquote, parse_qs
from typing import Optional

logger = logging.getLogger(__name__)

class URLResolver:
    """Resolve URLs redirecionadas e mal formadas"""
    
    def __init__(self):
        self.bing_redirect_pattern = re.compile(r'bing\.com/ck/a\?.*?&u=([^&]+)')
        
    def resolve_url(self, url: str) -> Optional[str]:
        """Resolve uma URL redirecionada para sua forma final"""
        
        if not url or not isinstance(url, str):
            return None
            
        try:
            # Limpar URL básica
            url = url.strip()
            
            # Resolver redirects do Bing
            if 'bing.com/ck/a' in url:
                resolved = self._resolve_bing_redirect(url)
                if resolved:
                    logger.info(f"🔗 URL Bing resolvida: {url[:50]}... -> {resolved[:50]}...")
                    return resolved
                else:
                    logger.warning(f"⚠️ Não foi possível resolver URL do Bing: {url[:100]}...")
                    return None
                    
            # Verificar se é uma URL válida
            parsed = urlparse(url)
            if not parsed.scheme or not parsed.netloc:
                logger.warning(f"⚠️ URL inválida: {url}")
                return None
                
            return url
            
        except Exception as e:
            logger.error(f"❌ Erro ao resolver URL {url}: {e}")
            return None
    
    def _resolve_bing_redirect(self, bing_url: str) -> Optional[str]:
        """Resolve redirects do Bing"""
        try:
            # Extrair parâmetro 'u' da URL do Bing
            match = self.bing_redirect_pattern.search(bing_url)
            if match:
                encoded_url = match.group(1)
                # Decodificar a URL
                decoded_url = unquote(encoded_url)
                
                # Converter de base64 se necessário
                if decoded_url.startswith('a1aHR0c'):
                    try:
                        import base64
                        decoded_bytes = base64.b64decode(decoded_url)
                        decoded_url = decoded_bytes.decode('utf-8')
                    except:
                        pass
                
                # Garantir que tem protocolo
                if decoded_url.startswith('://'):
                    decoded_url = 'https' + decoded_url
                elif not decoded_url.startswith(('http://', 'https://')):
                    decoded_url = 'https://' + decoded_url
                
                return decoded_url
                
        except Exception as e:
            logger.error(f"❌ Erro ao resolver redirect do Bing: {e}")
            
        return None
    
    def is_valid_url(self, url: str) -> bool:
        """Verifica se uma URL é válida"""
        try:
            if not url or not isinstance(url, str):
                return False
                
            parsed = urlparse(url)
            return bool(parsed.scheme and parsed.netloc)
            
        except:
            return False
    
    def clean_url(self, url: str) -> str:
        """Limpa uma URL removendo parâmetros desnecessários"""
        try:
            if not url:
                return url
                
            # Resolver primeiro se for redirect
            resolved = self.resolve_url(url)
            if not resolved:
                return url
                
            parsed = urlparse(resolved)
            
            # Manter apenas parâmetros essenciais
            essential_params = ['id', 'page', 'article', 'post', 'slug']
            
            if parsed.query:
                query_params = parse_qs(parsed.query)
                filtered_params = {}
                
                for param, values in query_params.items():
                    if param.lower() in essential_params:
                        filtered_params[param] = values
                
                if filtered_params:
                    from urllib.parse import urlencode
                    new_query = urlencode(filtered_params, doseq=True)
                    cleaned_url = f"{parsed.scheme}://{parsed.netloc}{parsed.path}?{new_query}"
                else:
                    cleaned_url = f"{parsed.scheme}://{parsed.netloc}{parsed.path}"
            else:
                cleaned_url = resolved
                
            return cleaned_url
            
        except Exception as e:
            logger.error(f"❌ Erro ao limpar URL: {e}")
            return url
