import requests
from bs4 import BeautifulSoup
from datetime import datetime

BASE_URL = "https://books.toscrape.com/"

def scrape_book(url: str) -> dict:
    resp = requests.get(url, timeout=10)
    resp.raise_for_status()

    soup = BeautifulSoup(resp.text, "html.parser")

    title = soup.find("h1").text.strip()
    price = soup.find("p", class_="price_color").text.strip()
    availability = soup.find("p", class_="instock availability").text.strip()

    breadcrumb = soup.select("ul.breadcrumb li a")
    category = breadcrumb[2].text.strip() if len(breadcrumb) > 2 else "Unknown"

    return {
        "name": title,
        "category": category,
        "price": price,
        "availability": availability,
        "vendor": "Books to Scrape",
        "url": url,
        "scraped_at": datetime.utcnow().isoformat()
    }
