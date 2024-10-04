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
    ```bash
    git clone https://github.com/YossefEzz/RecommendationSytemLLM_Llama3.git
    ```

2. Navigate to the project directory:
    ```bash
    cd Recommend_Sys
    ```

3. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

4. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

Here are some instructions and examples for using the project:

1. Start the Flask application:
    ```bash
    flask run
    ```

2. Open your browser and navigate to `http://localhost:5000` to see the application in action.

3. To get movie suggestions, you can use the `get_movie_suggestions` function from `utils.py`:
    ```python
    from utils import get_movie_suggestions
    import pandas as pd
    import faiss

    # Load your data and index
    df = pd.read_csv('path_to_your_data.csv')
    index = faiss.read_index('path_to_your_index')

    # Get suggestions
    favorite_text = "Your favorite movie description here"
    suggestions = get_movie_suggestions(favorite_text, 5, df, index)
    print(suggestions)
    ```

## Project Structure

Briefly describe the structure of your project. For example:
