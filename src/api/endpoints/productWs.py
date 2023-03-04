from fastapi import APIRouter

from src.core.models import Product

routeur = APIRouter()


@routeur.get("/")
async def hello_world():
    Product
    return {"message": "bonjour"}

