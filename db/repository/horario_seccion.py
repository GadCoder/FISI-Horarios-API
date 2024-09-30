from sqlalchemy.orm import Session
from sqlalchemy import text
from collections import defaultdict
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
        plan=horario_seccion.plan,
        aula=horario_seccion.aula,
        pabellon=horario_seccion.pabellon
    )
    db.add(horario_seccion)
    db.commit()
    db.refresh(horario_seccion)
    return horario_seccion



def get_hora_inicio_and_fin(horarios: list):
    if len(horarios) == 1:
        hora_inicio, hora_fin = horarios[0][0]
    else:
        hora_inicio = horarios[0][0][0]
        hora_fin = horarios[-1][0][1]
    return hora_inicio, hora_fin


def list_horarios_from_seccion(plan: str, carrera: str, codigo_seccion: str, db: Session):
    horarios_seccion = (
        db.query(HorarioSeccion)
        .filter(
            HorarioSeccion.plan == plan,
            HorarioSeccion.codigo_seccion == codigo_seccion,
            HorarioSeccion.carrera == carrera,
        )
        .all()
    )
    dias_dict = defaultdict(list)
    for horario in horarios_seccion:
        dias_dict[horario.dia].append(((horario.hora_inicio, horario.hora_fin), (horario.aula, horario.pabellon)))

    dias = []
    for dia, horarios in dias_dict.items():
        hora_inicio, hora_fin = get_hora_inicio_and_fin(horarios)
        aula, pabellon = horarios[0][1]
        dias.append({"dia": dia, 
                        "hora_inicio": hora_inicio, 
                        "hora_fin": hora_fin,
                        "aula": aula,
                        "pabellon": pabellon
                        })

    return {"codigo_seccion": codigo_seccion, "horarios": dias}
