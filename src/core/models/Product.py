from sqlalchemy import Column, Integer, String, PrimaryKeyConstraint, Float

from src.core.database.database import Base


class Product(Base):
    """
    Representation d'un produit
    """

    __tablename__ = "Product"
    product_id = Column(Integer, index=True, nullable=False, autoincrement=True)
    libelle = Column(String(144), nullable=False)
    prix = Column(Float, nullable=False)

    __table_args__ = (PrimaryKeyConstraint('product_id'),)
