from ingestion.chunker import Chunker
from rag.vactorstore import VectorStore

from dotenv import load_dotenv

load_dotenv()

content_list = [
    {"text": '''The Rise of Artificial Intelligence and Its Impact on the Future of Humanity
Introduction Artificial Intelligence (AI) has evolved from a theoretical concept discussed by scientists
and philosophers to a powerful force reshaping nearly every sector of modern society. Over the
past two decades, AI has advanced at a remarkable pace, driven by rapid improvements in
computational power, vast data availability, and sophisticated algorithms capable of learning from
experience. Today, AI systems can understand language, recognize images, analyze complex
data, and even create original content. These capabilities position AI not merely as a technological
tool but as a transformative catalyst that is redefining how we work, communicate, learn, and live.
1. The Evolution of Artificial Intelligence The origins of AI trace back to the mid-20th century. In
1956, at the Dartmouth Conference, John McCarthy and other pioneers proposed that machines
could one day simulate human intelligence. Early AI systems focused on symbolic
reasoning—manually encoding rules that machines could follow. These systems were rigid and
limited, but they laid foundational groundwork.
A major shift occurred in the 1980s and 1990s with the rise of machine learning, where computers
learned patterns from data rather than relying on predefined rules. The growth of the internet
provided enormous datasets, while developments in hardware—especially graphics processing
units (GPUs)—accelerated computation. In the 2010s, deep learning revolutionized AI by enabling
neural networks to identify extremely complex patterns. This breakthrough allowed AI systems to
surpass human performance in fields such as image recognition and language translation.
Today, we stand at a new frontier with generative AI, such as GPT-like systems, which can produce
human-level writing, images, code, and more. AI is no longer merely analyzing information; it is
creating it. This represents one of the most significant technological leaps since the invention of the
computer.
2. Key Areas Where AI Is Making an Impact Healthcare: AI is transforming healthcare by improving
diagnostic accuracy, predicting disease outbreaks, and assisting in personalized treatment
planning.
Education: AI-powered platforms personalize learning, automate tasks, and provide 24/7 AI tutoring
assistance.
Business: AI automates routine tasks, enhances customer service, and optimizes logistics.
Transportation: Self-driving cars and AI-optimized traffic systems are reshaping mobility.
Creativity: AI-generated art, music, and writing are expanding creative possibilities.
3. Benefits of AI AI increases efficiency, reduces costs, enhances accuracy, and drives innovation
across every industry.
4. Challenges and Ethical Concerns Despite its benefits, AI presents risks such as job loss, bias,
privacy violations, misinformation, and ethical dilemmas.
5. The Future of AI The future of AI depends on responsible development, global cooperation,
ethical regulation, and educating the next generation for an AI-driven world.
Conclusion Artificial Intelligence is one of the most transformative forces in human history. It offers
extraordinary potential but also demands careful oversight to ensure it remains aligned with human
values. With the right guidance, AI will empower societies, elevate human potential, and shape a
better future.''', "metadata": {"page_no": 1, "source": "document.pdf"}},
]


def invoke():
    chunker = Chunker()
    vector_store = VectorStore()

    # Chunk the content
    documents = chunker.chunk_document(content_list)

    # Add chunked documents to the vector store
    ids = vector_store.add_documents_to_vectorstore(documents)

    print(f"Added document IDs: {ids}")


if __name__ == "__main__":
    invoke()