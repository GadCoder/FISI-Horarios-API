from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
from schemas.HorarioSeccion import HorarioSeccionCreate
from db.session import get_db
from db.repository.horario_seccion import (
    create_new_horario_seccion,
    list_horarios_from_seccion,
)


router = APIRouter()


@router.post("/create-horario-seccion/")
def create_horario_seccion(
    horario_seccion: HorarioSeccionCreate, db: Session = Depends(get_db)
):
    horario_seccion = create_new_horario_seccion(horario_seccion=horario_seccion, db=db)
    return horario_seccion


@router.get("/get-horarios-from-seccion/{plan}/{carrera}/{codigo_seccion}")
def get_horarios_from_seccion(
    plan: str, carrera: str, codigo_seccion: str, db: Session = Depends(get_db)
):
    horarios_seccion = list_horarios_from_seccion(
        plan=plan,
        carrera=carrera, codigo_seccion=codigo_seccion, db=db
    )
    return horarios_seccion
