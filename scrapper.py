"""
Scraper module for fetching and cleaning text content from websites.
"""

import requests
from bs4 import BeautifulSoup


def fetch_website_contents(url: str) -> str:
    """
    Fetch raw HTML from a URL and extract clean, readable main text content.
    
    Args:
        url (str): The target website URL.
        
    Returns:
        str: Cleaned human-readable text content from the site.
        
    Raises:
        requests.RequestException: If the HTTP request fails.
    """
    # Use a standard browser User-Agent to avoid getting blocked by basic anti-bot rules
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0.0.0 Safari/537.36"
        )
    }

    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()

    # Parse HTML structure
    soup = BeautifulSoup(response.text, "html.parser")

    # Remove non-content tags that clutter the context window
    for tag in soup(["script", "style", "nav", "footer", "header", "noscript", "svg", "form"]):
        tag.decompose()

    # Prefer main content container if available, otherwise fall back to full body
    main_content = soup.find("main") or soup.find("article") or soup.body

    if not main_content:
        return ""

    # Extract text with space separators
    text = main_content.get_text(separator=" ", strip=True)

    # Collapse multiple whitespaces and line breaks into clean text
    cleaned_text = " ".join(text.split())

    return cleaned_text


if __name__ == "__main__":
    # Quick standalone test
    test_url = "https://example.com"
    print(f"Testing scraper on {test_url}...\n")
    try:
        content = fetch_website_contents(test_url)
        print("--- Scraped Output (First 500 chars) ---")
        print(content[:500])
    except Exception as e:
        print(f"Scraper error: {e}")
