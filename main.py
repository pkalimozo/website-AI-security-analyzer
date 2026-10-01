"""
Website Security Summarizer
Analyze and summarize security website contents, advisories, and threats using Ollama.
"""

import sys
from urllib.parse import urlparse
from openai import OpenAI, APIConnectionError, APIError
from scraper import fetch_website_contents

OLLAMA_BASE_URL = "http://localhost:11434/v1"
MODEL = "llama3.2"

# Structured system prompt instructing the model to extract security telemetry
SYSTEM_PROMPT = """
You are an expert Cybersecurity Analyst. Analyze the provided website content and deliver a clear, structured summary in raw Markdown.

Organize your output into the following sections (omit any section that has no relevant information):
- **Executive Summary**: A high-level overview of the site's main purpose/content.
- **Threats & Vulnerabilities**: Known CVEs, zero-days, exploit details, or attack vectors mentioned.
- **Incidents & Alerts**: Active breaches, security warnings, or urgent advisories.
- **News & Announcements**: Key security updates, press releases, or industry developments.
- **Actionable Recommendations**: Mitigations, patching advice, or defensive controls recommended by the site.

Constraints:
- Output raw, formatted Markdown only. Do NOT wrap the entire response in triple backticks (```markdown).
"""


def clean_url(url: str) -> str:
    """Ensure the URL has a proper scheme."""
    url = url.strip()
    if not url.startswith(("http://", "https://")):
        return f"https://{url}"
    return url


def get_client() -> OpenAI:
    """Initialize client outside the call loop for reuse."""
    return OpenAI(base_url=OLLAMA_BASE_URL, api_key="ollama")


def summarize(url: str, client: OpenAI) -> str:
    """Fetch website contents and generate a security summary via Ollama."""
    url = clean_url(url)
    
    print(f"[*] Fetching website: {url}...")
    try:
        website_content = fetch_website_contents(url)
        if not website_content or not website_content.strip():
            return "⚠️ Error: Website content was empty or could not be scraped."
    except Exception as e:
        return f"❌ Failed to fetch website: {e}"

    print(f"[*] Analyzing content with Ollama ({MODEL})...")
    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": f"Website Content:\n\n{website_content}"}
            ],
            temperature=0.2  # Low temperature keeps security summaries grounded and factual
        )
        return response.choices[0].message.content
    except APIConnectionError:
        return "❌ Error: Could not connect to Ollama. Make sure the server is running (`ollama serve`)."
    except APIError as e:
        return f"❌ Ollama API Error: {e}"


def main():
    """Main execution entry point."""
    print("=" * 50)
    print("        Website Security Summarizer (Ollama)      ")
    print("=" * 50)
    
    try:
        url = input("\nEnter website URL to analyze: ").strip()
        if not url:
            print("URL cannot be empty.")
            sys.exit(1)

        client = get_client()
        summary = summarize(url, client)
        
        print("\n" + "=" * 50)
        print("SECURITY SUMMARY RESULT")
        print("=" * 50 + "\n")
        print(summary)
        print("\n" + "=" * 50)

    except KeyboardInterrupt:
        print("\n[!] Operation cancelled by user.")
        sys.exit(0)


if __name__ == "__main__":
    main()