from ibm_watsonx_ai.metanames import GenTextParamsMetaNames as GenParams
from langchain_ibm import WatsonxLLM

def get_llm(project_id):
    """
    Load the IBM watsonx LLM model.

    Args:
        project_id (str): IBM watsonx project ID

    Returns:
        WatsonxLLM: LLM object
    """
    return WatsonxLLM(
        model_id="mistralai/mixtral-8x7b-instruct-v01",
        project_id=project_id,
        params={
            GenParams.MAX_NEW_TOKENS: 300,
            GenParams.TEMPERATURE: 0.5,
        }
    )