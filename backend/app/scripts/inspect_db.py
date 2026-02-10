from app.db.session import SessionLocal
from app.db.models import Vendor, Category, Product, PriceSnapshot

def inspect():
    db = SessionLocal()

    print("\nVENDORS")
    for v in db.query(Vendor).all():
        print(v.id, v.name)

    print("\nCATEGORIES")
    for c in db.query(Category).all():
        print(c.id, c.name)

    print("\nPRODUCTS")
    for p in db.query(Product).all():
        print(p.id, p.name, p.url)

    print("\nPRICE SNAPSHOTS")
    for s in db.query(PriceSnapshot).all():
        print(s.id, s.product_id, s.price, s.availability, s.scraped_at)

    db.close()

if __name__ == "__main__":
    inspect()
