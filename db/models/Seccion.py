from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db.base_class import Base


class Seccion(Base):
    id = Column(Integer, primary_key=True, index=True)
    carrera = Column(String)
    numero_seccion = Column(Integer)

    codigo_curso = Column(Integer, ForeignKey("curso.codigo_curso"))
    curso = relationship("Curso", back_populates="secciones")

    codigo_docente = Column(Integer, ForeignKey("docente.codigo_docente"))
    docente = relationship("Docente", back_populates="secciones")

    horarios = relationship("HorarioSeccion", back_populates="seccion")
