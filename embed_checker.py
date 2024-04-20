import json
import numpy as np
import torch
from sentence_transformers import util, SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

with open("embeddings_dict.json", "r") as f:
    embeddings_dict = json.load(f)

input_word = "Distace"
input_embeddings = model.encode(input_word, convert_to_tensor=True).float()

max_similarity = -1
correct_spelling = None
for word, embeddings in embeddings_dict.items():
    embeddings2 = np.array(embeddings, dtype=np.float32)
    embeddings2 = torch.tensor(embeddings2).float()
    cosine_scores = util.cos_sim(input_embeddings, embeddings2)
    similarity = cosine_scores.item()
    if similarity > max_similarity:
        max_similarity = similarity
        correct_spelling = word

print("Correct spelling:", correct_spelling)
