from fastapi import FastAPI
from db.base import Base
from fastapi.middleware.cors import CORSMiddleware
from db.session import engine
from apis.base import api_router


def create_tables():
    Base.metadata.create_all(bind=engine)


def include_router(app):
    app.include_router(api_router)


def add_cors(app):
    origins = ["*"]
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["GET"],
        allow_headers=["*"],
    )


def start_application():
    app = FastAPI()
    create_tables()
    include_router(app)
    add_cors(app)
    return app


app = start_application()
