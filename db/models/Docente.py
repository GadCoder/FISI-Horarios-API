from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from db.base_class import Base
from db.models import Seccion


class Docente(Base):
    id = Column(Integer, primary_key=True, index=True)
    codigo_docente = Column(String, unique=True)
    nombre = Column(String)
    apellido_paterno = Column(String)
    apellido_materno = Column(String)

    secciones = relationship("Seccion", back_populates="docente")

