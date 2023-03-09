from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.core import schemas
from src.core.database.database import get_db
from src.core.schemas.Product import Product
from src.core.service import ProductService

routeur = APIRouter()


# Obtention de tous les produits
@routeur.get("/", response_model=list[Product])
async def get_all_products(db : Session = Depends(get_db)):
    return ProductService.get_all_products(db)


# Obtention d'un produit via son ID
@routeur.get("/{id}", response_model=Product)
async def get_product_by_id(id: int):
    print('test')


# modification d'un Produit
@routeur.put("/{id}")
async def update_product_by_id(product: Product, id: int):
    print('test')


# suppression d'un produit via son id
@routeur.delete("/{id}")
async def delete_product_by_id(id: int):
    print('test')


# création d'un produit
@routeur.post("/")
async def create_product(product: Product):
    print('test')
