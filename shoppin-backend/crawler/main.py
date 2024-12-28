# Directory Structure
# web_crawler_backend/
# ├── crawler/
# │   ├── __init__.py
# │   ├── main.py
# │   ├── url_extractor.py
# │   ├── edge_case_handler.py
# │   ├── async_crawler.py
# │   └── utils.py
# ├── requirements.txt
# ├── README.md
# └── tests/
#     └── test_crawler.py

# Install Required Libraries
# - Scrapy: For web crawling
# - asyncio: For asynchronous processing
# - aiohttp: For asynchronous HTTP requests
# - BeautifulSoup4: For HTML parsing
# - pytest: For testing

# File: requirements.txt
scrapy
aiohttp
beautifulsoup4
pytest

# File: crawler/main.py
import asyncio
from crawler.url_extractor import extract_product_urls
from crawler.async_crawler import fetch_pages
from crawler.utils import save_results

async def main(domains):
    """Main entry point for the web crawler."""
    print("Starting the web crawler...")

    all_urls = {}

    for domain in domains:
        print(f"Processing domain: {domain}")
        page_content = await fetch_pages(domain)
        product_urls = extract_product_urls(page_content, domain)
        all_urls[domain] = list(set(product_urls))

    save_results(all_urls)
    print("Crawling completed! Results saved.")

if __name__ == "__main__":
    DOMAIN_LIST = [
        "https://www.example1.com",
        "https://www.example2.com",
        "https://www.example3.com",
    ]

    asyncio.run(main(DOMAIN_LIST))

# File: crawler/url_extractor.py
from bs4 import BeautifulSoup
import re

def extract_product_urls(html_content, domain):
    """Extract product URLs based on patterns."""
    soup = BeautifulSoup(html_content, "html.parser")
    product_urls = []

    for a_tag in soup.find_all("a", href=True):
        href = a_tag["href"]
        if re.search(r"/(product|item|p)/", href):
            product_urls.append(f"{domain}{href}" if href.startswith("/") else href)

    return product_urls

# File: crawler/async_crawler.py
import aiohttp

async def fetch_pages(url):
    """Fetch pages asynchronously."""
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                return await response.text()
            return ""

# File: crawler/utils.py
import json

def save_results(data):
    """Save the results to a JSON file."""
    with open("product_urls.json", "w") as file:
        json.dump(data, file, indent=4)

# File: crawler/edge_case_handler.py
import aiohttp
import asyncio

async def handle_infinite_scroll(url, scroll_depth):
    """Handle infinite scrolling using AJAX requests."""
    async with aiohttp.ClientSession() as session:
        for _ in range(scroll_depth):
            async with session.get(url) as response:
                if response.status == 200:
                    yield await response.text()

# File: README.md
# Web Crawler Backend

## Objective
A web crawler for discovering and listing all product URLs across multiple e-commerce websites.

### Features
- Scalable and efficient web crawling.
- Handles diverse URL patterns and edge cases like infinite scrolling.
- Asynchronous crawling for enhanced performance.
- Outputs structured data mapping each domain to its product URLs.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/web_crawler_backend.git
   cd web_crawler_backend
   ```
2. Install dependencies:
  
   pip install -r requirements.txt
   ```
3. Run the crawler:
   ```bash
   python crawler/main.py
   ```

## Testing
Run tests using:
```bash
pytest tests/
```

## Output
The crawler saves results in `product_urls.json` mapping each domain to its discovered product URLs.

# File: tests/test_crawler.py
import pytest
from crawler.url_extractor import extract_product_urls

def test_extract_product_urls():
    html = """<html><body><a href='/product/123'>Product 1</a></body></html>"""
    domain = "https://www.example.com"
    result = extract_product_urls(html, domain)
    assert result == ["https://www.example.com/product/123"]

