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
python -m pip install -r requirements.txt
```

## Configuration

Create a `.env` file in the repository root:

```dotenv
GOOGLE_API_KEY=your_gemini_api_key
```

Keep API keys out of source control. `.env` is already excluded by `.gitignore`.

## Run

Start Ollama and install `gemma3:270m` if you want the local Ollama request:

```powershell
ollama pull gemma3:270m
```

Then run the summarizer:

```powershell
Set-Location website-summarizer
python main.py
```

Change the URL passed to `fetch_website_contents(...)` in `main.py` to summarize another website.

## Chatbot Notebook

Start Jupyter from the repository root:

```powershell
jupyter notebook
```

Open `chatbot/main.ipynb` and select the project virtual environment as the notebook kernel.

## Troubleshooting

- Ensure the virtual environment is active and required packages are installed.
- Verify `GOOGLE_API_KEY` is set in `.env`.
- For Ollama errors, confirm Ollama is running on port `11434` and `gemma3:270m` is available.
