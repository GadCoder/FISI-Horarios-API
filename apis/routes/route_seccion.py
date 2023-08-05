from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends
from schemas.Seccion import SeccionCreate
from db.session import get_db
from db.repository.seccion import create_new_seccion


router = APIRouter()


@router.post("/")
def create_seccion(seccion: SeccionCreate, db: Session = Depends(get_db())):
    seccion = create_new_seccion(seccion=seccion, db=db)
    return seccion