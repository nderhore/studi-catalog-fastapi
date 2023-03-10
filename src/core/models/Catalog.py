from sqlalchemy import Integer, Column, Date, PrimaryKeyConstraint, String
from sqlalchemy.orm import relationship

from src.core.database.database import Base


class Catalog(Base):
    __tablename__ = "Catalog"
    catalog_id = Column(Integer, index=True, nullable=False, autoincrement=True)
    libelle = Column(String(144), nullable=False)
    date_debut = Column(Date, nullable=False)
    date_fin = Column(Date, nullable=False)
    products = relationship("Product", back_populates="catalog")

    __table_args__ = (PrimaryKeyConstraint('catalog_id'), {},)
