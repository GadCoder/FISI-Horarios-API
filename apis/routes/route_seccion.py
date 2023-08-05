from fastapi import APIRouter
from fastapi import HTTPException, status
from fastapi import Depends
from sqlalchemy.orm import Session
from schemas.Seccion import SeccionCreate
from db.session import get_db
from db.repository.seccion import create_new_seccion, delete_seccion, list_secciones, list_secciones_from_curso, delete_secciones

router = APIRouter()


@router.post("/create-seccion/{codigo_curso}/{codigo_docente}")
def create_seccion(seccion: SeccionCreate, codigo_curso: str, codigo_docente, db: Session = Depends(get_db)):
    seccion = create_new_seccion(seccion=seccion, codigo_curso=codigo_curso, codigo_docente=codigo_docente, db=db)
    return seccion


@router.get("/get-all-secciones")
def get_all_secciones(db: Session = Depends(get_db)):
    secciones = list_secciones(db=db)
    return secciones


@router.get("/get-secciones-from-curso/{codigo_curso}")
def get_secciones_from_curso(codigo_curso: str, db: Session = Depends(get_db)):
    secciones_curso = list_secciones_from_curso(codigo_curso=codigo_curso, db=db)
    return secciones_curso


@router.delete("/delete-seccion/{id}")
def delete_a_seccion(id: int, db: Session = Depends(get_db)):
    message = delete_seccion(id=id, db=db)
    if message.get("error"):
        raise HTTPException(detail=message.get("error"), status_code=status.HTTP_400_BAD_REQUEST)
    return {
        "message": f"Successfully deleted seccion with id {id}"
    }


@router.delete("/delete-all-secciones")
def delete_all_secciones(db: Session = Depends(get_db)):
    message = delete_secciones(db=db)
    if message.get("error"):
        raise HTTPException(detail=message.get("error"), status_code=status.HTTP_400_BAD_REQUEST)
    return {
        "message": f"Successfully deleted all secciones"
    }