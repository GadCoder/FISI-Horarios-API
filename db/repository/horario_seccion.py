
from sqlalchemy.orm import Session
from sqlalchemy import text
from schemas.HorarioSeccion import HorarioSeccionCreate
from db.models.HorarioSeccion import HorarioSeccion


def create_new_horario_seccion(horario_seccion: HorarioSeccionCreate, db: Session):
    horario_seccion = HorarioSeccion(
        hora_inicio=horario_seccion.hora_inicio,
        hora_fin=horario_seccion.hora_fin,
        dia=horario_seccion.dia,
        numero_horario=horario_seccion.numero_horario,
        carrera=horario_seccion.carrera,
        codigo_seccion=horario_seccion.codigo_seccion,

    )
    db.add(horario_seccion)
    db.commit()
    db.refresh(horario_seccion)
    return horario_seccion




def list_horarios_from_seccion(carrera: str, codigo_seccion: str, db: Session):
    horarios_seccion = db.query(HorarioSeccion).filter(HorarioSeccion.codigo_seccion == codigo_seccion,
                                                       HorarioSeccion.carrera == carrera).all()
    return horarios_seccion