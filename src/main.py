import os
from openai import OpenAI
from dotenv import load_dotenv
import re

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


def generate_prompt(article_content):
    """Prompt to generate HTML code."""

    prompt = f"""
    Przekształć poniższy artykuł w czysty kod HTML zgodny z wytycznymi.

    Artykuł:
    {article_content}

    Wytyczne dotyczące kodu HTML:
    - Traktuj krótkie fragmenty tekstu bez kropek na końcu jako tytuły sekcji.
    - Każdy tytuł rozpoczyna nową sekcję; dodaj nagłówek (np. <h1> lub <h2>).
    - Po nagłówku grupuj powiązane tematycznie fragmenty w jeden lub dwa dłuższe akapity, 
    aby zapewnić spójność treści w obrębie sekcji. Akapity zaczynaj od wcięcia w pierwszej linijce.
    - W każdej sekcji na jej początku umieść obrazek z src="image_placeholder.jpg" jako src.
    - Atrybut alt obrazka powinien zawierać dokładny prompt do generowania obrazu dla modelu. W szczególności:
      - Zastosuj opis, który jednoznacznie określa, co ma być widoczne na obrazie.
      - Do wygenerowania opisu przeanalizuj tekst sekcji.
      - Używaj pełnych zdań, np. "Wygeneruj obraz przedstawiający [główne elementy], 
      z uwzględnieniem [detale tła, nastrój, styl wizualny]".
    - Pod każdym obrazkiem dodaj krótki, bardzo zwięzły opis rysunku w tagu <figcaption> po polsku.
    - Jeśli w artykule występuje przypis, umieść go na końcu pliku, oznacz jako <footer> w osobnej sekcji.
    - Generuj tylko kod do wstawienia wewnątrz tagów <body>, bez dodatkowych tagów i sekcji. 
    - Pamiętaj o odpowiednim formatowaniu kodu.
    """
    return prompt


def generate_html_content(article_content):
    """Send a request to OpenAI to obtain HTML and filter the response."""
    prompt = generate_prompt(article_content)
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
    )

    # Extract clean HTML between the ``` tags
    match = re.search(r"```html\n(.*?)```", response.choices[0].message.content, re.DOTALL)

    if match:
        html_content = match.group(1).strip()  # Retrieves only the HTML content between the tags
        return html_content
    else:
        raise ValueError("Failed to extract HTML content from the response.")


def save_html_content(html_content, file_path):
    """Save the generated HTML to a file."""
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(html_content)


def main():
    # Load the article
    article_content = load_article_content(INPUT_FILE_PATH)

    # Generate HTML
    html_content = generate_html_content(article_content)

    # Save HTML to file
    save_html_content(html_content, OUTPUT_FILE_PATH)
    print(f"HTML has been saved to {os.path.abspath(OUTPUT_FILE_PATH)}")


if __name__ == "__main__":
    main()
