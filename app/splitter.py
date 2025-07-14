from langchain.text_splitter import RecursiveCharacterTextSplitter

def text_splitter(documents, chunk_size=1000, chunk_overlap=100):
    """
    Splits documents into manageable text chunks.

    Args:
        documents (List[Document]): List of documents to split
        chunk_size (int): Size of each text chunk
        chunk_overlap (int): Overlap between chunks

    Returns:
        List[Document]: Split documents
    """
    splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    return splitter.split_documents(documents)