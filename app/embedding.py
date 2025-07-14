from ibm_watsonx_ai.metanames import EmbedTextParamsMetaNames
from langchain_ibm import WatsonxEmbeddings

def get_embedding_model(project_id):
    """
    Loads IBM watsonx.ai embeddings.

    Args:
        project_id (str): IBM watsonx project ID

    Returns:
        WatsonxEmbeddings: Embedding model
    """
    return WatsonxEmbeddings(
        model_id="ibm/slate-125m-english-rtrvr",
        project_id=project_id,
        params={
            EmbedTextParamsMetaNames.TRUNCATE_INPUT_TOKENS: 3,
            EmbedTextParamsMetaNames.RETURN_OPTIONS: {"input_text": True},
        }
    )