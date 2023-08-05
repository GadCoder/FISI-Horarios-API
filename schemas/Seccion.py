from typing import Optional

from pydantic import BaseModel, Field
from schemas.Curso import Curso
from schemas.Docente import Docente
from schemas.HorarioSeccion import HorarioSeccion


class SeccionBase(BaseModel):
    numero_seccion: int


class SeccionCreate(SeccionBase):
    id: int
    carrera: str
    curso: Curso
    docente: Optional[Docente] = Field(None)
    pass


class Seccion(SeccionBase):
    horarios: list[HorarioSeccion] = []

    class Config:
        orm_mode = True
