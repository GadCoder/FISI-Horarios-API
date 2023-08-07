from fastapi import APIRouter
from apis.routes import route_curso
from apis.routes import route_docente
from apis.routes import route_seccion
from apis.routes import route_horario_seccion
from apis.routes import route_fronted

api_router = APIRouter()

api_router.include_router(route_fronted.router, prefix="")
api_router.include_router(route_curso.router, prefix="/cursos", tags=["cursos"])
api_router.include_router(route_docente.router, prefix="/docentes", tags=["docentes"])
api_router.include_router(route_seccion.router, prefix="/secciones", tags=["secciones"])
api_router.include_router(
    route_horario_seccion.router, prefix="/horario-seccion", tags=["horarios-secciones"]
)
