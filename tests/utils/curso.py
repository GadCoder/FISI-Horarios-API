from sqlalchemy.orm import Session
from db.repository.curso import create_new_curso
from schemas.Curso import CursoCreate


def create_random_curso(db: Session):
    curso = CursoCreate(
        carrera="SOFTWARE",
        ciclo=5,
        nombre_curso="ESTRUCTURA DE DATOS",
        codigo_curso="202W0505",
        creditaje=4,
        plan="2018"
    )
    curso_db = create_new_curso(curso=curso, db=db)
    return curso_db