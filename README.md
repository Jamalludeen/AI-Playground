# AI Playground

Small Python experiments for working with web content and language models.

This repository currently contains two related projects:

- **Website summarizer**: fetches a webpage, extracts readable text, and asks language models to summarize it.
- **Chatbot notebook**: an interactive chatbot experiment in Jupyter Notebook.

The website summarizer is the main documented workflow in this README.

## Repository layout

```text
.
├── chatbot/
│   ├── main.ipynb       # Jupyter chatbot experiment
│   └── scrapper.py      # Web scraping helpers used by the notebook
├── website-summarizer/
│   ├── main.py          # Website summarizer entry point
│   └── scrapper.py      # HTML fetching and text extraction helpers
├── .env                 # Local secrets; ignored by Git
└── README.md
```

Run commands for the summarizer from `website-summarizer/`, because `main.py`
imports the sibling module `scrapper.py`.

## What it does

The website summarizer currently follows this flow:

1. Fetch `https://www.udemy.com` with a browser-like user agent.
2. Remove scripts, styles, images, and form inputs from the page.
3. Extract the page title and visible body text, limited to 2,000 characters.
4. Send that content to a local Ollama-compatible endpoint.
5. Send the same content to the Gemini OpenAI-compatible endpoint.
6. Print the Gemini response in the terminal.

The generated response is requested in Markdown with sections for the website
overview, main offerings, target audience, key features, and a short summary.


## Scraper behavior

`website-summarizer/scrapper.py` exposes two helper functions:

- `fetch_website_contents(url)` performs an HTTP GET, parses HTML with
	Beautiful Soup, removes common non-content elements, and returns the title
	plus visible text truncated to 2,000 characters.
- `fetch_website_links(url)` returns non-empty `href` values from page links.

Both helpers use a browser-like `User-Agent` header. They currently do not set
timeouts, call `raise_for_status()`, normalize relative links, or handle
network and parsing exceptions. Those are useful next improvements if this
experiment becomes a reusable service.

## Prerequisites

- Python 3.10 or newer.
- Internet access for fetching the target webpage and calling Gemini.
- An API key for the Gemini-compatible endpoint.
- [Ollama](https://ollama.com/) running locally at `http://localhost:11434` if
  you want the local request in `main.py` to succeed.
- The Ollama model `gemma3:270m` available locally:

  ```powershell
  ollama pull gemma3:270m
  ```

## Installation

From the repository root, create and activate a virtual environment, then
install the packages imported by the summarizer:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install beautifulsoup4 requests python-dotenv openai
```

For the chatbot notebook, install Jupyter as well:

```powershell
python -m pip install jupyter
```

There is currently no `requirements.txt` or `pyproject.toml`; the commands
above are the source-of-truth dependency setup for the current code.

## Configuration

Create a `.env` file in the repository root:

```dotenv
GOOGLE_API_KEY=your_gemini_api_key
```

`main.py` loads this value with `python-dotenv` and passes it to the
OpenAI-compatible Gemini client. Do not commit real credentials. The existing
`.gitignore` excludes `.env` from version control.

The current endpoint and model values are defined directly in
`website-summarizer/main.py`:

- Gemini base URL: `https://generativelanguage.googleapis.com/v1beta/openai/`
- Gemini model: `gemini-4-hydrogen`
- Ollama URL: `http://localhost:11434/v1/chat/completions`
- Ollama model: `gemma3:270m`

## Run the website summarizer

1. Start Ollama and make sure `gemma3:270m` is installed.
2. Activate the virtual environment.
3. From the summarizer directory, run:

   ```powershell
   Set-Location website-summarizer
   python main.py
   ```

The target URL is currently hard-coded as `https://www.udemy.com` in
`main.py`. The script prints the Gemini-generated Markdown summary. The local
Ollama response is currently created but not printed because its print
statement is commented out.

To summarize another page, change the URL passed to
`fetch_website_contents(...)` in `website-summarizer/main.py`.

## Open the chatbot notebook

The chatbot experiment lives in `chatbot/main.ipynb`. From the repository
root, start Jupyter after installing the notebook dependencies:

```powershell
jupyter notebook
```

Then open `chatbot/main.ipynb` and select the virtual environment as its
kernel. The notebook has its own `chatbot/scrapper.py`; it is separate from
the scraper used by the website summarizer.

The summarizer sends the Ollama request and the Gemini request independently,
but the Ollama request is made before the Gemini request. A failed local
Ollama service can therefore stop the script before Gemini is called.

## Troubleshooting

### `ModuleNotFoundError`

Activate the virtual environment and install the packages from the
Installation section. Run `python -m pip show openai requests beautifulsoup4`
to confirm they are installed in the active interpreter.

### Gemini authentication fails

Check that `.env` is in the repository root, that it contains
`GOOGLE_API_KEY`, and that the key is valid for the configured Gemini
OpenAI-compatible endpoint.

### Ollama connection fails

Start Ollama, verify that it is listening on port `11434`, and confirm the
model name with `ollama list`. The current script does not catch request
errors, so connection failures appear as Python exceptions.

### The summary is incomplete

The scraper intentionally limits extracted content to 2,000 characters and
removes several HTML elements. Pages that render most content with JavaScript
may not provide that content in the initial HTTP response.

## Contributing

Keep changes focused and update this README when commands, endpoints, models,
or project structure change. Before opening a pull request:

```powershell
python -m compileall website-summarizer chatbot
git diff --check
```

The repository does not yet include automated tests or a dependency lockfile.
