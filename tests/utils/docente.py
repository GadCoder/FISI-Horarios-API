from sqlalchemy.orm import Session
from db.repository.docente import create_new_docente
from schemas.Docente import DocenteCreate


def create_random_docente(db: Session):
    docente = DocenteCreate(
        codigo_docente='2020123',
        nombre="JAIME",
        apellido_paterno="PARIONA",
        apellido_materno="QUISPE"
    )
    docente_db = create_new_docente(docente=docente, db=db)
    return docente_db