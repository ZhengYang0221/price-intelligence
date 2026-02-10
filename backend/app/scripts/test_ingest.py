from app.scraper.books import scrape_book
from app.services.ingest import ingest_scraped_book
from app.db.session import SessionLocal

def run():
    db = SessionLocal()
    try:
        data = scrape_book(
            "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
        )
        ingest_scraped_book(db, data)
        print("Ingestion successful")
    finally:
        db.close()

if __name__ == "__main__":
    run()
