from pydantic import BaseModel
from datetime import date

class Prestamo(BaseModel):
    IDPrestamo: int
    IDLibro: int
    FechaPrestamo: date
    FechaDevolucion: date