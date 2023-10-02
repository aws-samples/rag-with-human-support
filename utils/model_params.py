"""
Utilities for modeling
"""


def get_model_params(
    model_id: str,
    params: dict,
) -> dict:
    """
    Set up a dictionary with model parameters named appropriately for Bedrock

    Parameters
    ----------
    model_id : str
        Model name
    params : dict
        Inference parameters

    Returns
    -------
    dict
        _description_
    """

    model_params = {}

    # name parameters based on the model id
    if model_id.startswith("amazon"):
        model_params = {
            "maxTokenCount": params["answer_length"],
            "stopSequences": params["stop_words"],
            "temperature": params["temperature"],
            "topP": params["top_p"],
        }
    elif model_id.startswith("anthropic"):
        model_params = {
            "max_tokens_to_sample": params["answer_length"],
            "stop_sequences": params["stop_words"],
            "temperature": params["temperature"],
            "top_p": params["top_p"],
        }
    elif model_id.startswith("ai21"):
        model_params = {
            "maxTokens": params["answer_length"],
            "stopSequences": params["stop_words"],
            "temperature": params["temperature"],
            "topP": params["top_p"],
        }

    return model_params
