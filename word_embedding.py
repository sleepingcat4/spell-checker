import json
from sentence_transformers import SentenceTransformer
from tqdm import tqdm
import concurrent.futures

model = SentenceTransformer("all-MiniLM-L6-v2")

def generate_embedding(word):
    embeddings = model.encode(word, convert_to_tensor=True)
    return word, embeddings.tolist()

word_file = "word_processed.txt"
with open(word_file, "r") as f:
    words = f.read().splitlines()

embeddings_dict = {}
with concurrent.futures.ThreadPoolExecutor() as executor:
    future_to_word = {executor.submit(generate_embedding, word): word for word in words}
    for future in tqdm(concurrent.futures.as_completed(future_to_word), total=len(words), desc="Generating embeddings"):
        word = future_to_word[future]
        try:
            word, embedding = future.result()
            embeddings_dict[word] = embedding
        except Exception as exc:
            print(f"Error generating embedding for {word}: {exc}")

output_file = "embeddings_dict.json"
with open(output_file, "w") as f:
    json.dump(embeddings_dict, f)
