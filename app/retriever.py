from .loader import document_loader
from .splitter import split_documents
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
    chunks = split_documents(documents)
    embeddings = get_embedding_model(project_id)
    return create_vectorstore(chunks, embeddings)
