from sqlalchemy.orm import Session
from db.repository.horario_seccion import create_new_horario_seccion
from schemas.HorarioSeccion import HorarioSeccionCreate
from tests.utils.seccion import create_random_seccion

def create_random_horario_seccion(db: Session):
    seccion = create_random_seccion(db=db)
    horario_seccion = HorarioSeccionCreate(
        hora_inicio=8,
        hora_fin=12,
        dia="LUNES",
        carrera="SOFTWARE",
        codigo_seccion=seccion.codigo_seccion,
        numero_horario=1,
        plan="2018"
    )
    horario_seccion_db = create_new_horario_seccion(horario_seccion=horario_seccion, db=db)
    return horario_seccion_db
