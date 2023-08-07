from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from db.base import Base
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
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


templates = Jinja2Templates(directory="templates")

app = start_application()


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    ciclos = range(1, 11)
    return templates.TemplateResponse(
        "index.html", {"request": request, "ciclos": ciclos}
    )
