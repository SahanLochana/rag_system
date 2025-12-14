from langchain_google_genai import GoogleGenerativeAIEmbeddings


class Config:
    CHUNK_SIZE = 1000
    CHUNK_OVERLAP = 200

    EMBEDDING_MODEL = "models/gemini-embedding-001"
    PERSIST_DIR = "./vector_stores/chromaDB"
    COLLECTION_NAME = "slides_collection"