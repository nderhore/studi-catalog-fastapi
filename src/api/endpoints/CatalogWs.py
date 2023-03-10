from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.core.database.database import get_db
from src.core.schemas.Catalog import Catalog
from src.core.service import CatalogService

routeur = APIRouter()


@routeur.get("/", response_model=list[Catalog])
async def get_all_catalogs(db: Session = Depends(get_db)):
    return CatalogService.get_all_catalogs(db)
