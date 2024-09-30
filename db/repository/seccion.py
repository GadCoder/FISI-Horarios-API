from sqlalchemy import text
from sqlalchemy.orm import Session
from schemas.Seccion import SeccionCreate
from db.models.Seccion import Seccion


def create_new_seccion(seccion: SeccionCreate, codigo_curso: str, codigo_docente: str, db: Session):
    seccion = Seccion(**seccion.dict(), codigo_curso=codigo_curso, codigo_docente=codigo_docente)
    db.add(seccion)
    db.commit()
    db.refresh(seccion)
    return seccion


def list_secciones(db: Session):
    secciones = db.query(Seccion).all()
    return secciones


def list_secciones_from_curso(plan: str, codigo_curso: str, db: Seccion):
    secciones_curso = db.query(Seccion).filter(Seccion.plan == plan,  Seccion.codigo_curso == codigo_curso).all()
    return secciones_curso


def delete_seccion(id: int, db: Session):
    seccion_in_db = db.query(Seccion).filter(Seccion.id == id)
    if not seccion_in_db.first():
        return {"error": f"Could not find seccion with id {id}"}
    seccion_in_db.delete()
    db.commit()
    return {"message": f"deleted seccion with id {id}"}


def delete_secciones(db: Session):
    try:
        db.execute(text("DELETE FROM Seccion;"))
        db.commit()
        return {"message": "All rows deleted successfully"}
    except Exception as e:
        db.rollback()
        return {"error": "An error ocurred"}
    finally:
        db.close()

