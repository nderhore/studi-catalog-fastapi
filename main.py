from fastapi import FastAPI

from src.api import api
from src.core.database.database import Base, engine

app = FastAPI(title='Studi')

app.include_router(api.routeur, prefix='/api')
Base.metadata.create_all(engine)
