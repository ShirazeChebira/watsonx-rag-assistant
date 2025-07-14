from langchain.chains import RetrievalQA

def create_qa_chain(llm, retriever):
    """
    Build the QA chain using LangChain.

    Args:
        llm: Language model
        retriever: Retriever object

    Returns:
        RetrievalQA
    """
    return RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        return_source_documents=False
    )