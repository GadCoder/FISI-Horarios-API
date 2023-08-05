from fastapi import APIRouter
from apis.routes import route_curso
from apis.routes import route_docente

api_router = APIRouter()
api_router.include_router(route_curso.router, prefix="/cursos", tags=["cursos"])
api_router.include_router(route_docente.router, prefix="/docentes", tags=["docentes"])
