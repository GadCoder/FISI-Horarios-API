from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db.base_class import Base


class HorarioSeccion(Base):
    id = Column(Integer, primary_key=True, index=True)
    hora_inicio = Column(Integer)
    hora_fin = Column(Integer)
    dia = Column(String)
    numero_horario = Column(Integer)
    carrera = Column(String)
    codigo_seccion = Column(String, ForeignKey("seccion.codigo_seccion"))
    seccion = relationship("Seccion", back_populates="horarios")

