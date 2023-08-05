from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db.base_class import Base


class Seccion(Base):
    id = Column(Integer, primary_key=True, index=True)
    codigo_seccion = Column(String, unique=True)
    numero_seccion = Column(Integer)

    carrera = Column(String)

    codigo_curso = Column(String, ForeignKey("curso.codigo_curso"))
    curso = relationship("Curso", back_populates="secciones")

    codigo_docente = Column(String, ForeignKey("docente.codigo_docente"))
    docente = relationship("Docente", back_populates="secciones")

    horarios = relationship("HorarioSeccion", back_populates="seccion")
