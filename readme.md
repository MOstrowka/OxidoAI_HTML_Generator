# Oxido_AI_HTML_Generator

Aplikacja pobiera treść z pliku tekstowego, wysyła ją do modelu GPT-4o, który generuje kod HTML zgodny z wytycznymi.

## Instalacja

1. Klonowanie repozytorium:
   ```bash
   git clone OxidoAI_HTML_Generator
   cd Oxido_AI_HTML_Generator
   ```

2. Instalacja bibliotek:
   ```bash
   pip install -r requirements.txt
   ```

3. Utwórz plik `.env` w głównym folderze projektu i dodaj swój klucz API OpenAI:
   ```plaintext
   OPENAI_API_KEY=your_openai_api_key
   ```

## Uruchomienie aplikacji

1. Przejdź do katalogu `src`:
   ```bash
   cd src
   ```
2. Uruchom skrypt `main.py`:
   ```bash
   python main.py
   ```

Wygenerowany plik HTML znajdziesz w folderze `output` jako `artykul.html`.

## Dodatkowe pliki

Projekt zawiera również pliki `szablon.html` oraz `podglad.html`.

- **szablon.html**: Zawieraj stylizację i strukturę, do której dołączana jest treść artykułu.
  
- **podglad.html**: Plik `podglad.html` ładuje `szablon.html` oraz `artykul.html`, wyświetlając całą treść artykułu zgodnie z ustaloną stylizacją. Używa JavaScript do dynamicznego osadzenia treści artykułu w szablonie.
