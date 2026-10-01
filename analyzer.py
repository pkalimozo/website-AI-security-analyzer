"""
Website summarizer using Ollama instead of OpenAI.
"""

from openai import OpenAI
from scraper import fetch_website_contents

OLLAMA_BASE_URL = "http://localhost:11434/v1"
MODEL = "llama3.2"

system_prompt = """
You are a helpful Cyber Security Analyst that analyzes the contents of a website,
and provides a short, summary of the website.
If it includes news or announcements, then summarize these too.
If it includes vulnerabilities, then summarize these too.
If it includes threats, then summarize these too.
If it includes recommendations, then summarize these too.
If it includes warnings, then summarize these too.
If it includes alerts, then summarize these too.
If it includes incidents, then summarize these too.
Respond in markdown. Do not wrap the markdown in a code block - respond just with the markdown.
"""

user_prompt_prefix = """
Here are the contents of a website.
Provide a short summary of this website.
If it includes news or announcements, then summarize these too.
If it includes vulnerabilities, then summarize these too.
If it includes threats, then summarize these too.
If it includes recommendations, then summarize these too.
If it includes warnings, then summarize these too.
If it includes alerts, then summarize these too.
If it includes incidents, then summarize these too.
"""


def messages_for(website):
    """Create message list for the LLM."""
    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt_prefix + website}
    ]


def summarize(url):
    """Fetch and summarize a website using Ollama."""
    ollama = OpenAI(base_url=OLLAMA_BASE_URL, api_key='ollama')
    website = fetch_website_contents(url)
    response = ollama.chat.completions.create(
        model=MODEL,
        messages=messages_for(website)
    )
    return response.choices[0].message.content
    

def main():
    """Main entry point for testing."""
    url = input("Enter a URL to summarize: ")
    print("\nFetching and summarizing...\n")
    summary = summarize(url)
    print(summary)


if __name__ == "__main__":
    main()
