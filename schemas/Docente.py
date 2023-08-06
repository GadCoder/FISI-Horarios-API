from typing import Optional
from pydantic import BaseModel, Field


class DocenteBase(BaseModel):
    codigo_docente: str
    nombre: Optional[str] = Field(None)
    apellido_paterno: Optional[str] = Field(None)
    apellido_materno: Optional[str] = Field(None)


class DocenteCreate(DocenteBase):
    pass


class Docente(DocenteBase):
    id: int

    class Config:
        orm_mode = True
