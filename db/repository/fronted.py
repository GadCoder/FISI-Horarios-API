from sqlalchemy.orm import Session
from db.models.Curso import Curso
from db.models.HorarioSeccion import HorarioSeccion
from db.repository.horario_seccion import list_horarios_from_seccion
from fastapi import Request


def add_curso(request: Request, db: Session, codigo_curso: str, codigo_seccion: str):
    curso = db.query(Curso).filter(Curso.codigo_curso == codigo_curso).first()
    nombre_curso = curso.nombre_curso
    creditaje = curso.creditaje
    horarios_seccion = list_horarios_from_seccion()
    request.session["creditaje"] += creditaje

    request.session["cursos-agregados"].append(
        {"nombre_curso": nombre_curso, "horarios-seccion": horarios_seccion}
    )
