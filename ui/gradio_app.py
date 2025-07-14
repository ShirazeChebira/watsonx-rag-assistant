import gradio as gr
from app.llm import get_llm
from app.retriever import get_retriever
from app.qa_chain import create_qa_chain
import os

PROJECT_ID = os.getenv("WATSONX_PROJECT_ID")

def ask_question(file, query):
    try:
        llm = get_llm(PROJECT_ID)
        retriever = get_retriever(file.name, PROJECT_ID)
        qa_chain = create_qa_chain(llm, retriever)
        result = qa_chain.invoke(query)
        return result["result"]
    except Exception as e:
        return f"❌ Error: {e}"

def launch_app():
    gr.Interface(
        fn=ask_question,
        inputs=[
            gr.File(label="Upload PDF File", file_types=[".pdf"], type="file"),
            gr.Textbox(label="Enter your question")
        ],
        outputs=gr.Textbox(label="Answer"),
        title="📄 Watsonx PDF QA Chatbot",
        description="Upload a PDF and ask questions using a RAG assistant powered by Watsonx.ai + LangChain."
    ).launch(share=True)