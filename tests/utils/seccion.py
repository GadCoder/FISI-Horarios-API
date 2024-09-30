from sqlalchemy.orm import Session

from db.repository.seccion import create_new_seccion
from schemas.Seccion import SeccionCreate

from .curso import create_random_curso
from .docente import create_random_docente


def create_random_seccion(db: Session):
    curso = create_random_curso(db=db)
    docente = create_random_docente(db=db)
    seccion = SeccionCreate(
        codigo_seccion="123",
        numero_seccion=1,
        carrera="SOFTWARE",
        plan="2018"
    )
    seccion_db = create_new_seccion(seccion=seccion, 
                                    db=db, 
                                    codigo_curso=curso.codigo_curso, 
                                    codigo_docente=docente.codigo_docente)
    return seccion_db