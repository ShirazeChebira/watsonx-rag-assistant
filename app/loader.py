from langchain_community.document_loaders import PyPDFLoader

def document_loader(file_path):
    """
    Loads PDF file using LangChain's PyPDFLoader.
    
    Args:
        file_path (str): Path to the PDF file

    Returns:
        List[Document]: List of LangChain documents
    """
    loader = PyPDFLoader(file_path)
    return loader.load()