from pydantic import BaseModel, validator


class ProductBase(BaseModel):
    product_id: int = None
    libelle: str
    prix: float
    catalog_id: int = None


class ProductUpdate(BaseModel):
    pass


class ProductCreate(ProductBase):
    pass


class Product(ProductBase):

    @validator("product_id", pre=True)
    def product_id_is_primary_key(cls, value):
        return value

    class Config:
        orm_mode = True
