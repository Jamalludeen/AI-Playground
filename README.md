# AI Playground

Small Python experiments for web scraping and AI-generated responses.

- `website-summarizer/` fetches a webpage and summarizes its content with Gemini and Ollama.
- `chatbot/` contains a Jupyter Notebook chatbot experiment.

## Website Summarizer

The script fetches `https://www.udemy.com`, extracts up to 2,000 characters of page text, and asks a language model for a structured Markdown summary.

## Setup

Python 3.10 or newer is recommended.

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install beautifulsoup4 requests python-dotenv openai
```

For the chatbot notebook, also install Jupyter:

```powershell
python -m pip install jupyter
```
