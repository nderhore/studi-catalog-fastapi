import datetime

from pydantic import BaseModel, validator


class CatalogBase(BaseModel):
    catalog_id: int = None
    libelle: str
    date_debut: datetime.datetime
    date_fin: datetime.datetime


class CatalogUpdate(BaseModel):
    pass


class CatalogCreate(CatalogBase):
    pass


class Catalog(CatalogBase):

    @validator("catalog_id", pre=True)
    def catalog_id_is_primary_key(cls, value):
        return value

    class Config:
        orm_mode = True
