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
