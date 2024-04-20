from huggingface_hub import notebook_login
notebook_login()

import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

model_checkpoint = "google/gemma-2b-it"

tokenizer = AutoTokenizer.from_pretrained(model_checkpoint)

model = AutoModelForCausalLM.from_pretrained(model_checkpoint, torch_dtype=torch.bfloat16, device_map="cuda")

def correct_spelling(word, model, tokenizer):
    prompt = f"is '{word}' correct spelling?"

    token_inputs = tokenizer(prompt, return_tensors="pt").to('cuda')

    token_outputs = model.generate(input_ids=token_inputs['input_ids'], max_new_tokens=150, do_sample=True, temperature=0.5)
    decoded_output = tokenizer.decode(token_outputs[0], skip_special_tokens=True)

    print("Model's response:")
    print(decoded_output)
