from .loader import document_loader
from .splitter import text_splitter
from .embedding import get_embedding_model
from .vectordb import create_vectorstore


def get_retriever(file_path, project_id):
    """
    Full pipeline to create a retriever from a PDF file.

    Args:
        file_path (str): Path to the PDF file
        project_id (str): IBM watsonx project ID

    Returns:
        VectorStoreRetriever
    """
    documents = document_loader(file_path)
    chunks = text_splitter(documents)
    embeddings = watsonx_embedding(project_id)
    return build_vectorstore(chunks, embeddings)