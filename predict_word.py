from happytransformer import HappyWordPrediction

happy_wp = HappyWordPrediction()

def predict_word(prompt: str, model, top_k: int = 2) -> list[str]:
    # Add [MASK] to the prompt
    text = prompt + " [MASK]"

    # Predict the masked word
    result = model.predict_mask(text, top_k=top_k)

    # Extract token values from the result
    predictions = [prediction.token for prediction in result]

    return predictions
