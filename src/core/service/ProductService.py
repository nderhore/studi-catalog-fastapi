from sqlalchemy.orm import Session

from src.core.models.Product import Product


def get_all_products(db : Session):
    return db.query(Product).all()

