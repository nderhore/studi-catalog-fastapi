from sqlalchemy import Integer, Column, PrimaryKeyConstraint
from sqlalchemy.orm import relationship

from src.core.database.database import Base


class Sales(Base):
    __tablename__ = "Sales"

    sales_id = Column(Integer, index=True, nullable=False, autoincrement=True)
    remise = Column(Integer, nullable=False)
    produits = relationship("Product")

    __table_args__ = (PrimaryKeyConstraint('catalog_id'),)
