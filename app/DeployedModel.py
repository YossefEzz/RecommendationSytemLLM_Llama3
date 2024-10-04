import logging
from flask import Flask, request, jsonify, render_template
import pandas as pd
import numpy as np
import faiss
import requests
from llama_index.embeddings.ollama import OllamaEmbedding

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Load the data and FAISS index
df = pd.read_csv(r"data\netflix_titles.csv")
index = faiss.read_index(r"data\index")

def create_textual_representation(row):
    txt = f"""Type: {row['type']},
Title: {row['title']},
Director: {row['director']},
Cast: {row['cast']},
Release Year: {row['release_year']},

Description: {row['description']}"""
    return txt

df['textual_representation'] = df.apply(create_textual_representation, axis=1)

def get_movie_suggestions(favorite_text, num_suggestions=5):
    try:
        logging.debug(f"Generating embedding for text: {favorite_text}")
        embedding_model = OllamaEmbedding(model_name="llama3.2")
        embedding = embedding_model.get_text_embedding (favorite_text)
        logging.debug(f"Generated embedding: {embedding}")
        embedding = np.array(embedding, dtype="float32")
        D, I = index.search(embedding.reshape(1, -1), num_suggestions)
        best_matches = df.iloc[I[0]]
        return best_matches
    except Exception as e:
        logging.error(f"Embedding generation failed: {e}")
        return pd.DataFrame()  # Return an empty DataFrame on failure

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/suggest', methods=['POST'])
def suggest():
    data = request.json
    favorite_text = data.get('favorite_text')
    num_suggestions = int(data.get('num_suggestions', 5))  # Convert to integer
    suggestions = get_movie_suggestions(favorite_text, num_suggestions)
    suggestions = suggestions.fillna('')  # Replace NaN values with empty strings
    suggestions_dict = suggestions.to_dict(orient='records')  # Convert DataFrame to list of dictionaries
 
    return jsonify(suggestions_dict)

if __name__ == '__main__':
    app.run(debug=True)