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
