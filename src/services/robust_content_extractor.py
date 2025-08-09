#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ARQV30 Enhanced v2.0 - Robust Content Extractor CORRIGIDO
Extrator de conteúdo ultra-robusto com múltiplos engines
"""

import logging
import time
import requests
from typing import Dict, List, Optional, Tuple, Any
import re
from urllib.parse import urlparse, urljoin
from .url_resolver import URLResolver

logger = logging.getLogger(__name__)

class RobustContentExtractor:
    """Extrator de conteúdo robusto com múltiplos engines"""

    def __init__(self):
        """Inicializa o extrator com múltiplos engines"""
        self.available_extractors = []
        self.url_resolver = URLResolver()
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'pt-BR,pt;q=0.9,en;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1'
        })

        self._initialize_extractors()

    def _initialize_extractors(self):
        """Inicializa todos os extratores disponíveis"""

        # Trafilatura
        try:
            import trafilatura
            self.available_extractors.append('trafilatura')
        except ImportError:
            logger.warning("⚠️ Trafilatura não disponível")

        # Readability
        try:
            from readability import Document
            self.available_extractors.append('readability')
        except ImportError:
            logger.warning("⚠️ Readability não disponível")

        # Newspaper3k
        try:
            import newspaper
            self.available_extractors.append('newspaper')
        except ImportError:
            logger.warning("⚠️ Newspaper3k não disponível")

        # BeautifulSoup
        try:
            from bs4 import BeautifulSoup
            self.available_extractors.append('beautifulsoup')
        except ImportError:
            logger.warning("⚠️ BeautifulSoup não disponível")

        # PyPDF2 para PDFs
        try:
            import PyPDF2
            self.available_extractors.append('pdf_pypdf2')
        except ImportError:
            logger.warning("⚠️ PyPDF2 não disponível")

        # pdfplumber para PDFs
        try:
            import pdfplumber
            self.available_extractors.append('pdf_pdfplumber')
        except ImportError:
            logger.warning("⚠️ pdfplumber não disponível")

        # PyMuPDF para PDFs
        try:
            import fitz  # PyMuPDF
            self.available_extractors.append('pdf_pymupdf')
        except ImportError:
            logger.warning("⚠️ PyMuPDF não disponível")

        logger.info(f"🔧 Robust Content Extractor inicializado")
        logger.info(f"📚 Extratores disponíveis: {self.available_extractors}")

    def extract_content(self, url: str, timeout: int = 30) -> Tuple[str, Dict[str, Any]]:
        """Extrai conteúdo de uma URL com múltiplos métodos"""

        if not url:
            return "", {"error": "URL vazia"}

        # Resolver URL primeiro
        resolved_url = self.url_resolver.resolve_url(url)
        if not resolved_url:
            logger.warning(f"⚠️ URL não pôde ser resolvida: {url}")
            return "", {"error": "URL não resolvida"}

        logger.info(f"🔍 INICIANDO EXTRAÇÃO REAL de: {resolved_url}")

        # Verificar se é PDF
        if self._is_pdf_url(resolved_url):
            logger.info("📄 PDF detectado - usando extratores especializados")
            return self._extract_pdf_content(resolved_url, timeout)

        # Extrair conteúdo HTML
        return self._extract_html_content(resolved_url, timeout)

    def _is_pdf_url(self, url: str) -> bool:
        """Verifica se a URL aponta para um PDF"""
        return url.lower().endswith('.pdf') or 'pdf' in url.lower()

    def _extract_html_content(self, url: str, timeout: int) -> Tuple[str, Dict[str, Any]]:
        """Extrai conteúdo de páginas HTML"""

        metadata = {"url": url, "extractors_tried": [], "extractor_used": None}

        # Baixar HTML
        try:
            html_content = self._download_html(url, timeout)
            if not html_content:
                return "", {"error": "Falha ao baixar HTML"}

            logger.info(f"📥 HTML baixado: {len(html_content)} caracteres")

        except Exception as e:
            logger.error(f"❌ Erro ao baixar {url}: {e}")
            return "", {"error": f"Erro no download: {str(e)}"}

        # Tentar extração com cada método disponível
        for extractor_name in self.available_extractors:
            if extractor_name.startswith('pdf_'):
                continue  # Skip PDF extractors for HTML

            try:
                metadata["extractors_tried"].append(extractor_name)
                logger.info(f"🔍 Tentando extração com {extractor_name}...")

                content = self._extract_with_method(html_content, extractor_name, url)

                if content and len(content.strip()) > 100:
                    extraction_time = time.time()
                    logger.info(f"✅ Extração bem-sucedida com {extractor_name}: {len(content)} caracteres em {extraction_time - time.time():.2f}s")
                    metadata["extractor_used"] = extractor_name
                    metadata["content_length"] = len(content)
                    return content, metadata
                else:
                    logger.warning(f"⚠️ Conteúdo insuficiente com {extractor_name}: {len(content) if content else 0} caracteres")

            except Exception as e:
                logger.warning(f"⚠️ Erro com {extractor_name}: {e}")
                continue

        # Se todos falharam, tentar extração agressiva
        logger.warning("⚠️ Todos os extratores padrão falharam, tentando extração agressiva...")
        try:
            aggressive_content = self._aggressive_extraction(html_content)
            if aggressive_content and len(aggressive_content.strip()) > 50:
                metadata["extractor_used"] = "aggressive"
                return aggressive_content, metadata
        except Exception as e:
            logger.error(f"❌ Extração agressiva falhou: {e}")

        logger.error(f"❌ FALHA CRÍTICA: Todos os extratores falharam para {url}")
        return "", {"error": "Todos os extratores falharam"}

    def _download_html(self, url: str, timeout: int) -> str:
        """Baixa o conteúdo HTML de uma URL"""

        for attempt in range(3):
            try:
                response = self.session.get(url, timeout=timeout, allow_redirects=True)
                response.raise_for_status()
                return response.text

            except Exception as e:
                logger.error(f"❌ Erro ao baixar {url} (tentativa {attempt + 1}): {e}")
                if attempt < 2:
                    time.sleep(2 ** attempt)
                else:
                    raise

        logger.error(f"❌ Falha ao baixar HTML para {url}")
        return ""

    def _extract_with_method(self, html_content: str, method: str, url: str) -> str:
        """Extrai conteúdo usando um método específico"""

        if method == 'trafilatura':
            import trafilatura
            return trafilatura.extract(html_content) or ""

        elif method == 'readability':
            from readability import Document
            doc = Document(html_content)
            return doc.summary()

        elif method == 'newspaper':
            import newspaper
            from newspaper import Article
            article = Article(url)
            article.set_html(html_content)
            article.parse()
            return article.text or ""

        elif method == 'beautifulsoup':
            from bs4 import BeautifulSoup
            soup = BeautifulSoup(html_content, 'html.parser')

            # Remover scripts e estilos
            for script in soup(["script", "style"]):
                script.decompose()

            # Extrair texto
            text = soup.get_text()

            # Limpar texto
            lines = (line.strip() for line in text.splitlines())
            chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
            text = '\n'.join(chunk for chunk in chunks if chunk)

            return text

        return ""

    def _aggressive_extraction(self, html_content: str) -> str:
        """Extração agressiva como último recurso"""
        try:
            from bs4 import BeautifulSoup
            soup = BeautifulSoup(html_content, 'html.parser')

            # Remover elementos indesejados
            for element in soup(['script', 'style', 'nav', 'header', 'footer', 'aside']):
                element.decompose()

            # Buscar por containers de conteúdo
            content_selectors = [
                'article', '.content', '.post', '.entry', '#content',
                '.main', '.article-body', '.post-content', 'main'
            ]

            for selector in content_selectors:
                elements = soup.select(selector)
                if elements:
                    content = ' '.join(elem.get_text().strip() for elem in elements)
                    if len(content) > 100:
                        return content

            # Se nada funcionou, pegar todo o texto
            return soup.get_text()

        except Exception as e:
            logger.error(f"❌ Erro na extração agressiva: {e}")
            return ""

    def _extract_pdf_content(self, url: str, timeout: int) -> Tuple[str, Dict[str, Any]]:
        """Extrai conteúdo de PDFs"""

        metadata = {"url": url, "extractors_tried": [], "extractor_used": None}

        try:
            # Baixar PDF
            response = self.session.get(url, timeout=timeout)
            response.raise_for_status()
            pdf_content = response.content

            logger.info(f"📄 PDF baixado: {len(pdf_content)} bytes")

        except Exception as e:
            logger.error(f"❌ Erro ao processar PDF {url}: {e}")
            return "", {"error": f"Erro no download do PDF: {str(e)}"}

        # Tentar extração com múltiplos métodos
        for extractor in ['pdf_pdfplumber', 'pdf_pymupdf', 'pdf_pypdf2']:
            if extractor not in self.available_extractors:
                continue

            try:
                metadata["extractors_tried"].append(extractor)
                content = self._extract_pdf_with_method(pdf_content, extractor)

                if content and len(content.strip()) > 100:
                    logger.info(f"✅ PDF extraído com {extractor.replace('pdf_', '').title()}: {len(content)} caracteres")
                    metadata["extractor_used"] = extractor
                    metadata["content_length"] = len(content)
                    return content, metadata

            except Exception as e:
                logger.warning(f"⚠️ Erro com {extractor}: {e}")
                continue

        return "", {"error": "Falha na extração do PDF"}

    def _extract_pdf_with_method(self, pdf_content: bytes, method: str) -> str:
        """Extrai texto de PDF usando método específico"""

        import io

        if method == 'pdf_pdfplumber':
            import pdfplumber
            with io.BytesIO(pdf_content) as pdf_file:
                with pdfplumber.open(pdf_file) as pdf:
                    text = ""
                    for page in pdf.pages:
                        page_text = page.extract_text()
                        if page_text:
                            text += page_text + "\n"
                    return text

        elif method == 'pdf_pymupdf':
            import fitz
            with io.BytesIO(pdf_content) as pdf_file:
                pdf_doc = fitz.open(stream=pdf_file, filetype="pdf")
                text = ""
                for page in pdf_doc:
                    text += page.get_text() + "\n"
                pdf_doc.close()
                return text

        elif method == 'pdf_pypdf2':
            import PyPDF2
            with io.BytesIO(pdf_content) as pdf_file:
                reader = PyPDF2.PdfReader(pdf_file)
                text = ""
                for page in reader.pages:
                    text += page.extract_text() + "\n"
                return text

        return ""

    def get_stats(self) -> Dict[str, Any]:
        """Retorna estatísticas do extrator"""
        return {
            "available_extractors": self.available_extractors,
            "total_extractors": len(self.available_extractors),
            "pdf_extractors": len([e for e in self.available_extractors if e.startswith('pdf_')]),
            "html_extractors": len([e for e in self.available_extractors if not e.startswith('pdf_')])
        }


# Instância global para uso em toda a aplicação
robust_content_extractor = RobustContentExtractor()