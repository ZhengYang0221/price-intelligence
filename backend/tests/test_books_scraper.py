from app.scraper.books import scrape_book

def test_scrape_book():
    data = scrape_book(
        "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
    )

    assert "name" in data
    assert "price" in data
    assert "availability" in data
    assert data["vendor"] == "Books to Scrape"
