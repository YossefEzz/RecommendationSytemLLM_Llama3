import requests
import numpy as np

def create_textual_representation(row):
    txt = f"""Type: {row['type']},
Title: {row['title']},
Director: {row['director']},
Cast: {row['cast']},
Release Year: {row['release_year']},

Description: {row['description']}"""
    return txt

def get_movie_suggestions(favorite_text, num_suggestions, df, index):
    res = requests.post("http://localhost:11434/api/embeddings", json={"model": "llama3.2", "prompt": favorite_text})
    embedding = np.array(res.json()['embedding'], dtype="float32")
    D, I = index.search(embedding.reshape(1, -1), num_suggestions)
    best_matches = np.array(df.iloc[I[0]]['title'])
    return best_matches