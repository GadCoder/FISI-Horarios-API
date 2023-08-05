from fastapi import FastAPI
from db.base import Base
from db.session import engine
from apis.base import api_router


def create_tables():
    Base.metadata.create_all(bind=engine)


def include_router(app):
    app.include_router(api_router)


def start_application():
    app = FastAPI()
    create_tables()
    include_router(app)
    return app


app = start_application()


@app.get("/")
async def root():
    return {"message": "Hello World"}
