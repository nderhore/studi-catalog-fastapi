from fastapi import APIRouter

routeur = APIRouter()


@routeur.get("/")
async def hello_world():
    return {"message": "bonjour"}
