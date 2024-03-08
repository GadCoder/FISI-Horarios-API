from typing import Optional

from pydantic import BaseModel
from schemas.HorarioSeccion import HorarioSeccion


class SeccionBase(BaseModel):
    codigo_seccion: str
    numero_seccion: int
    carrera: str
    plan: str


class SeccionCreate(SeccionBase):
    pass


class Seccion(SeccionBase):
    id: int
    horarios: list[HorarioSeccion] = []

    class Config:
        orm_mode = True
