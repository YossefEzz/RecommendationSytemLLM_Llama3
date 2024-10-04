# Recommend_Sys

Recommend_Sys is a recommendation system designed to provide movie suggestions based on user preferences using machine learning models.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Workflow](#workflow)
- [Training Process](#training-process)
- [Output](#output)
- [Contributing](#contributing)
- [License](#license)

## Installation

Follow these steps to set up the project locally:

1. Clone the repository:
    \\\ash
    git clone https://github.com/YossefEzz/RecommendationSytemLLM_Llama3.git
    \\\

2. Navigate to the project directory:
    \\\ash
    cd Recommend_Sys
    \\\

3. Create a virtual environment and activate it:
    \\\ash
    python -m venv venv
    source venv/bin/activate  # On Windows use \env\Scripts\activate\
    \\\

4. Install the dependencies:
    \\\ash
    pip install -r requirements.txt
    \\\

## Usage

Here are some instructions and examples for using the project:

1. Start the Flask application:
    \\\ash
    flask run
    \\\

2. Open your browser and navigate to \http://localhost:5000\ to see the application in action.

3. To get movie suggestions, you can use the \get_movie_suggestions\ function from \utils.py\:
    \\\python
    from utils import get_movie_suggestions
    import pandas as pd
    import faiss

    # Load your data and index
    df = pd.read_csv('path_to_your_data.csv')
    index = faiss.read_index('path_to_your_index')

    # Get suggestions
    favorite_text = \
Your
favorite
movie
description
here\
    suggestions = get_movie_suggestions(favorite_text, 5, df, index)
    print(suggestions)
    \\\

## Project Structure

Briefly describe the structure of your project. 


Recommend_Sys/
├── data/           # Data files
├── models/         # Machine learning models
├── src/            # Source code
│   ├── components/ # Flask components
│   ├── services/   # Services and utilities
│   └── app.py      # Main application file
├── tests/          # Unit tests
├── app/utils.py    # Utility functions
├── requirements.txt# Project dependencies
├── .gitignore      # Git ignore file
└── README.md       # This file


## Workflow

1. **Data Collection**: Collect movie data including title, director, cast, release year, and description.
2. **Textual Representation**: Use the \create_textual_representation\ function to create a textual representation of each movie.
3. **Embedding Generation**: Send the textual representation to an embedding API to get a numerical representation (embedding) of the text.
4. **Indexing**: Use FAISS to index the embeddings for efficient similarity search.
5. **Recommendation**: Use the \get_movie_suggestions\ function to find the most similar movies based on the user's favorite movie description.

## Training Process

1. **Data Preparation**: Prepare the dataset with relevant movie information.
2. **Embedding Model**: Use a pre-trained language model (e.g., LLaMA) to generate embeddings for the movie descriptions.
3. **Indexing**: Index the embeddings using FAISS for efficient similarity search.
4. **Evaluation**: Evaluate the recommendation system using metrics like precision, recall, and F1-score.

## Output

The output of the recommendation system is a list of movie titles that are most similar to the user's favorite movie description.



## Contributing

We welcome contributions! Follow these steps to contribute:

1. Fork the repository.
2. Create a new branch for your feature or bugfix:
    \\\ash
    git checkout -b feature-branch
    \\\

3. Make your changes.
4. Commit your changes:
    \\\ash
    git commit -m 'Add some feature'
    \\\

5. Push to the branch:
    \\\ash
    git push origin feature-branch
    \\\

6. Open a pull request on GitHub.


