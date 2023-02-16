from fastapi import FastAPI

from src.api import api

app = FastAPI(title='Studi')

app.include_router(api.routeur, prefix='/api')
