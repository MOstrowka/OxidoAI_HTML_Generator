import os
from openai import OpenAI
from dotenv import load_dotenv

# Load env
load_dotenv()

# OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# File paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_FILE_PATH = os.path.relpath("../data/artykul.txt", BASE_DIR)
OUTPUT_FILE_PATH = os.path.relpath("../output/artykul.html", BASE_DIR)


def load_article_content(file_path):
    """Load article content from file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


def main():
    # Load the article
    article_content = load_article_content(INPUT_FILE_PATH)
    print(article_content)


if __name__ == "__main__":
    main()