from fastapi import FastAPI
from db.base import Base
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from starlette.middleware.sessions import SessionMiddleware
from db.session import engine
from apis.base import api_router


def create_tables():
    Base.metadata.create_all(bind=engine)


def include_router(app):
    app.include_router(api_router)


def mount_static_folder(app):
    app.mount("/static", StaticFiles(directory="static"), name="static")


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
    mount_static_folder(app)
    add_cors(app)
    return app


app = start_application()
