def predict_word(prompt: str, model, tokenizer, top_k: int = 2) -> list[str]:
    # Add [MASK] to the prompt
    text = prompt + " [MASK]"

    result = model.predict_mask(text, top_k=top_k)

    predictions = [prediction.token for prediction in result]

    return predictions
