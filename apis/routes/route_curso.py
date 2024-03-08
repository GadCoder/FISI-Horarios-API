from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from fastapi import Depends
from schemas.Curso import CursoCreate
from db.session import get_db
from db.repository.curso import (
    create_new_curso,
    retreive_curso,
    list_cursos,
    delete_curso,
    list_cursos_from_carrera,
    list_cursos_from_ciclo,
)


router = APIRouter()


@router.post("/create-curso/")
def create_curso(curso: CursoCreate, db: Session = Depends(get_db)):
    curso = create_new_curso(curso=curso, db=db)
    return curso


@router.get("/get-curso/{codigo_curso}")
def get_curso(codigo_curso: str, db: Session = Depends(get_db)):
    curso = retreive_curso(codigo_curso=codigo_curso, db=db)
    if not curso:
        raise HTTPException(
            detail=f"Curso with ID {id} does not exist.",
            status_code=status.HTTP_404_NOT_FOUND,
        )
    return curso


@router.get("/get-all-cursos/")
def get_all_cursos(db: Session = Depends(get_db)):
    cursos = list_cursos(db=db)
    return cursos


@router.get("/get-cursos-from-carrera/{plan}/{carrera}")
def get_cursos_from_carrera(plan: str, carrera: str, db: Session = Depends(get_db)):
    cursos_carrera = list_cursos_from_carrera(plan=plan, carrera=carrera, db=db)
    return cursos_carrera


@router.get("/get-from-ciclo/{plan}/{carrera}/{ciclo}")
def get_cursos_from_ciclo(plan: str, carrera: str, ciclo: int, db: Session = Depends(get_db)):
    cursos_ciclo = list_cursos_from_ciclo(plan=plan, carrera=carrera, ciclo=ciclo, db=db)
    return cursos_ciclo



