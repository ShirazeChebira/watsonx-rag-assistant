from langchain_community.vectorstores import Chroma

def create_vectorstore(chunks, embeddings):
    """
    Creates a Chroma vector store from text chunks and embeddings.

    Args:
        chunks (List[Document]): List of text chunks
        embeddings (Embeddings): Embedding model

    Returns:
        VectorStoreRetriever: Retriever object
    """
    vectordb = Chroma.from_documents(chunks, embeddings)
    return vectordb.as_retriever()