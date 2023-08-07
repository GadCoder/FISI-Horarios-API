from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from db.base import Base
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from db.session import engine
from apis.base import api_router


def create_tables():
    Base.metadata.create_all(bind=engine)


def include_router(app):
    app.include_router(api_router)


def mount_static_folder(app):
    app.mount("/static", StaticFiles(directory="static"), name="static")


def start_application():
    app = FastAPI()
    create_tables()
    include_router(app)
    mount_static_folder(app)
    return app


templates = Jinja2Templates(directory="templates")

app = start_application()


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    ciclos = range(1, 11)
    return templates.TemplateResponse(
        "index.html", {"request": request, "ciclos": ciclos}
    )
