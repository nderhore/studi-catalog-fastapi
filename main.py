from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from src.api import api
from src.core.database.database import Base, engine


origins = [
    "http://localhost:4200"
]


app = FastAPI(title='Studi')

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api.routeur, prefix='/api')
Base.metadata.create_all(engine)
