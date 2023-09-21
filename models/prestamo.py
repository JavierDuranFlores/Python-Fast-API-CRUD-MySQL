from sqlalchemy import Column, Integer, Date
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Prestamo(Base):
    __tablename__ = 'Prestamos'  # Nombre de la tabla en la base de datos

    IDPrestamo = Column(Integer, primary_key=True, index=True)
    IDLibro = Column(Integer,index=True)
    FechaPrestamo = Column(Date)
    FechaDevolucion = Column(Date)