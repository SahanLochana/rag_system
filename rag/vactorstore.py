from langchain_chroma import Chroma
from core.config import Config
from langchain_google_genai import GoogleGenerativeAIEmbeddings


class VectorStore:
    def __init__(self):
        try:
            embedding_func = GoogleGenerativeAIEmbeddings(model=Config.EMBEDDING_MODEL)
            self.vectorestore = Chroma(
            collection_name=Config.COLLECTION_NAME,
            embedding_function=embedding_func,
            persist_directory=Config.PERSIST_DIR,)
        except Exception as e:
            print(f"Error initializing Chroma vector store: {e}")
            raise
    
    def add_documents_to_vectorstore(self, documents):
        try:
            ids = self.vectorestore.add_documents(documents)
            return ids
        
        except Exception as e:
            print(f"couldn't add documents {e}")