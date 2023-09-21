from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Libro(Base):
    __tablename__ = "Libros";
    
    IDLibro =  Column(Integer, primary_key=True, index=True, unique=True, nullable=True)
    Titulo = Column(String(255), nullable=True)
    Autor = Column(String(255), nullable=True)
    AnioPublicacion = Column(Integer, nullable=True)