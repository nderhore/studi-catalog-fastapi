from sqlalchemy.orm import Session

from src.core.models.Catalog import Catalog


def get_all_catalogs(db: Session):
    return db.query(Catalog).all()
