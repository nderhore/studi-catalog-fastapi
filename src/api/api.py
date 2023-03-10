from fastapi import APIRouter

from src.api.endpoints import productWs, CatalogWs, SalesWs

routeur = APIRouter()
routeur.include_router(productWs.routeur, prefix='/product',
                       tags=["product"],
                       responses={404 : {"description":"Impossible"}})

routeur.include_router(CatalogWs.routeur, prefix='/catalog',
                       tags=["catalog"],
                       responses={404 : {"description":"Impossible"}})

routeur.include_router(SalesWs.routeur, prefix='/sales',
                       tags=["sales"],
                       responses={404 : {"description":"Impossible"}})


