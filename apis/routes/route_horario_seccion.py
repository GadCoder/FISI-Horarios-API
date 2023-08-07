from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
from schemas.HorarioSeccion import HorarioSeccionCreate
from db.session import get_db
from db.repository.horario_seccion import create_new_horario_seccion, list_horarios_from_seccion
from collections import defaultdict


router = APIRouter()


@router.post("/create-horario-seccion/")
def create_horario_seccion(horario_seccion: HorarioSeccionCreate, db: Session = Depends(get_db)):
    horario_seccion = create_new_horario_seccion(horario_seccion=horario_seccion, db=db)
    return horario_seccion


@router.get("/get-horarios-from-seccion/{carrera}/{codigo_seccion}")
def get_horarios_from_seccion(carrera: str, codigo_seccion: str, db: Session = Depends(get_db)):
    horarios_seccion = list_horarios_from_seccion(carrera=carrera, codigo_seccion=codigo_seccion, db=db)
    codigo_seccion = ""
    dias_dict = defaultdict(list)
    for horario in horarios_seccion:
        hora_inicio = horario.hora_inicio
        hora_fin = horario.hora_fin
        dia = horario.dia
        codigo_seccion = horario.codigo_seccion
        dias_dict[dia].append((
            hora_inicio, hora_fin
        ))

    dias = []
    for dia, horarios in dias_dict.items():
        if len(horarios) == 1:
            hora_inicio, hora_fin = horarios[0]
        else:
            hora_inicio = horarios[0][0]
            hora_fin = horarios[-1][1]

        dias.append({
            "dia": dia,
            "hora_inicio": hora_inicio,
            "hora_fin": hora_fin
        })

    return {
        "codigo_seccion": codigo_seccion,
        "horarios": dias
    }


