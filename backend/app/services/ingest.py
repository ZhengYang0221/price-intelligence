import re
from sqlalchemy.orm import Session
from datetime import datetime

from app.db.models import Vendor, Category, Product, PriceSnapshot


def ingest_scraped_book(db: Session, data: dict):
    # Vendor
    vendor = db.query(Vendor).filter_by(name=data["vendor"]).first()
    if not vendor:
        vendor = Vendor(name=data["vendor"])
        db.add(vendor)
        db.commit()
        db.refresh(vendor)

    # Category
    category = db.query(Category).filter_by(name=data["category"]).first()
    if not category:
        category = Category(name=data["category"])
        db.add(category)
        db.commit()
        db.refresh(category)

    # Product
    product = db.query(Product).filter_by(url=data["url"]).first()
    if not product:
        product = Product(
            name=data["name"],
            url=data["url"],
            vendor_id=vendor.id,
            category_id=category.id,
        )
        db.add(product)
        db.commit()
        db.refresh(product)

    # Price snapshot (robust parsing)
    price_str = data["price"]
    price_value = float(re.sub(r"[^\d.]", "", price_str))

    snapshot = PriceSnapshot(
        product_id=product.id,
        price=price_value,
        availability=data["availability"],
        scraped_at=datetime.fromisoformat(data["scraped_at"]),
    )

    db.add(snapshot)
    db.commit()
