from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from core.config import Config

class Chunker:

    """
    Split PDF page texts into smaller LangChain Document chunks.

    Uses RecursiveCharacterTextSplitter with sizes from Config.
    Expects a list of dicts like:
        {"text": "<page text>", "metadata": {...}}

    Returns a flat list of Documents where:
        - page_content = chunk text
        - metadata     = original page metadata (e.g. page_no, source)
    """

    def __init__(self):
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=Config.CHUNK_SIZE,
            chunk_overlap=Config.CHUNK_OVERLAP,
            separators=["\n\n", "\n", " ", ""]
        )

    def chunk_document(self, pdf_contents: list[dict[str,dict[str,any]]]) -> list[Document]:
        chunked_docs = []
        for page_content in pdf_contents:
            texts = self.text_splitter.split_text(page_content['text'])
            for text in texts:
                chunked_docs.append(
                    Document(
                        page_content=text,
                        metadata=page_content['metadata']
                    )
                )
        return chunked_docs
    