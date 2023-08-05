from typing import Optional

from pydantic import BaseModel, Field
from schemas.Curso import Curso
from schemas.Docente import Docente
from schemas.HorarioSeccion import HorarioSeccion


class SeccionBase(BaseModel):
    codigo_seccion: str
    numero_seccion: int
    carrera: str


class SeccionCreate(SeccionBase):
    pass


class Seccion(SeccionBase):
    id: int
    horarios: list[HorarioSeccion] = []

    class Config:
        orm_mode = True
