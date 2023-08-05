from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from db.base_class import Base


class Curso(Base):
    id = Column(Integer, primary_key=True, index=True)
    carrera = Column(String)
    ciclo = Column(Integer)
    nombre_curso = Column(String)
    codigo_curso = Column(String, unique=True)
    creditaje = Column(Integer)

    secciones = relationship("Seccion", back_populates="curso")
