from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from db.repository.fronted import add_curso
from db.session import get_db

router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get("/", response_class=HTMLResponse)
async def root(request: Request):
    ciclos = range(1, 11)
    dias = ["LUNES", "MARTES", "MIERCOLES", "JUEVES", "VIERNES", "SABADO"]
    horas = [f"{hora}:00-{hora + 1}:00" for hora in range(8, 22)]
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "ciclos": ciclos, "dias": dias, "horas": horas},
    )


@router.get("/add-selected-curso/{codigo_curso}/{seccion}")
def add_selected_curso(
    request: Request,
    codigo_curso: str,
    codigo_seccion: str,
    db: Session = Depends(get_db),
):
    add_curso(
        request=request, db=db, codigo_curso=codigo_curso, codigo_seccion=codigo_seccion
    )
