from scrapper import fetch_website_contents, fetch_website_links
import requests


udemy = fetch_website_contents("https://www.udemy.com")

system_prompt = """
You are a snarky assistant that analyzes the contents of a website,
and provides a short, snarky, humorous summary, ignoring text that might be navigation related.
Respond in markdown. Do not wrap the markdown in a code block - respond just with the markdown.
"""

response = requests.post(
    "http://localhost:11434/v1/chat/completions",
    json={
        "model": "gemma3:270m",
        "messages": [{"role": "system", "content": system_prompt + ' ' + udemy}],
    }
)
print(response.json()["choices"][0]["message"]["content"])