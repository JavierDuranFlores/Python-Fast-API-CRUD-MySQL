from pydantic import BaseModel
from sqlalchemy import Column, Integer, String

class Libro(BaseModel):
    IDLibro: int
    Titulo: str
    Autor: str
    AnioPublicacion: int