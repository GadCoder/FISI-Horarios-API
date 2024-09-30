from pydantic import BaseModel


class CursoCreate(BaseModel):
    carrera: str
    ciclo: int
    nombre_curso: str
    codigo_curso: str
    creditaje: int
    plan: str


class Curso(BaseModel):
    id: int

    class Config:
        orm_mode = True
