from sqlalchemy.orm import Session
from schemas.Curso import CursoCreate
from db.models.Curso import Curso


def create_new_curso(curso: CursoCreate, db: Session):
    curso = Curso(
        carrera=curso.carrera,
        ciclo=curso.ciclo,
        nombre_curso=curso.nombre_curso,
        codigo_curso=curso.codigo_curso,
        creditaje=curso.creditaje
    )
    db.add(curso)
    db.commit()
    db.refresh(curso)
    return curso


def retreive_curso(id: int, db: Session):
    curso = db.query(Curso).filter(Curso.id == id).first()
    return curso


def list_cursos(db: Session):
    cursos = db.query(Curso).all()
    return cursos


def list_cursos_from_carrera(carrera: str, db: Session):
    cursos_carrera = db.query(Curso).filter(Curso.carrera == carrera).all()
    return cursos_carrera


def list_cursos_from_ciclo(carrera: str, ciclo: int, db: Session):
    cursos_ciclo = db.query(Curso).filter(Curso.carrera == carrera, Curso.ciclo == ciclo).all()
    return cursos_ciclo


def delete_curso(id: int, db: Session):
    curso_in_db = db.query(Curso).filter(Curso.id == id)
    if not curso_in_db.first():
        return {"error": f"Could not find curso with id {id}"}
    curso_in_db.delete()
    db.commit()
    return {"message": f"deleted curso with id {id}"}
