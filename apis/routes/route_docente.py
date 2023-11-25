from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from fastapi import Depends
from schemas.Docente import DocenteCreate
from db.session import get_db
from db.repository.docente import create_new_docente, retreive_docente, delete_docente, list_docentes, delete_docentes

router = APIRouter()


@router.post("/create-docente/")
def create_docente(docente: DocenteCreate, db: Session = Depends(get_db)):
    codigo_docente = docente.codigo_docente
    docente = create_new_docente(docente=docente, db=db)
    if not docente:
        raise HTTPException(detail=f"Docente with codigo {codigo_docente} already in database.", status_code=status.HTTP_409_CONFLICT)
    return docente


@router.get("/get-docente/{id}")
def get_curso(id: int, db: Session = Depends(get_db)):
    docente = retreive_docente(id=id, db=db)
    if not docente:
        raise HTTPException(detail=f"Docente with ID {id} does not exist.", status_code=status.HTTP_404_NOT_FOUND)
    return docente


@router.get("/get-all-docentes/")
def get_all_docentes(db: Session = Depends(get_db)):
    docentes = list_docentes(db=db)
    return docentes


