from pydantic import BaseModel


class HorarioSeccionBase(BaseModel):
    hora_inicio: int
    hora_fin: int
    dia: str


class HorarioSeccionCreate(HorarioSeccionBase):
    pass


class HorarioSeccion(HorarioSeccionBase):
    id: int

    class Config:
        orm_mode = True
