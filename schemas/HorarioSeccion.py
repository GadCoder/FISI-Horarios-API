from pydantic import BaseModel
from schemas.Seccion import Seccion


class HorarioSeccionBase(BaseModel):
    hora_inicio: int
    hora_fin: int
    dia: str


class HorarioSeccionCreate(HorarioSeccionBase):
    pass


class HorarioSeccion(HorarioSeccionBase):
    id: int
    seccion = Seccion

    class Config:
        orm_mode = True
