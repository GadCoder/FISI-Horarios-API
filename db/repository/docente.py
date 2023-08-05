
from sqlalchemy.orm import Session
from sqlalchemy import text
from schemas.Docente import DocenteCreate
from db.models.Docente import Docente


def create_new_docente(docente: DocenteCreate, db: Session):
    docente_in_db = db.query(Docente).filter(Docente.codigo_docente == docente.codigo_docente).first()
    if docente_in_db:
        return None

    docente = Docente(
        codigo_docente=docente.codigo_docente,
        nombre=docente.nombre,
        apellido_paterno=docente.apellido_paterno,
        apellido_materno=docente.apellido_materno
    )
    db.add(docente)
    db.commit()
    db.refresh(docente)
    return docente


def retreive_docente(id: int, db: Session):
    curso = db.query(Docente).filter(Docente.id == id).first()
    return curso


def list_docentes(db: Session):
    docentes = db.query(Docente).all()
    return docentes


def delete_docente(id: int, db: Session):
    docente_in_db = db.query(Docente).filter(Docente.id == id)
    if not docente_in_db.first():
        return {"error": f"Could not find docente with id {id}"}
    docente_in_db.delete()
    db.commit()
    return {"message": f"deleted docente with id {id}"}


def delete_docentes(db: Session):
    try:
        db.execute(text("DELETE FROM Docente;"))
        db.commit()
        return {"message": "All rows deleted successfully"}
    except Exception as e:
        db.rollback()
        return {"error": "An error ocurred"}
    finally:
        db.close()

