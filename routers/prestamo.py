from fastapi import FastAPI, APIRouter, HTTPException
from config.db import SessionLocal
from schemas.prestamo import Prestamo, PrestamoAll
from models.prestamo import Prestamo as PS
from models.libro import Libro as LS
from sqlalchemy import text
from typing import List
from sqlalchemy import join
from sqlalchemy.sql import select

prestamo = APIRouter()

db = SessionLocal()

@prestamo.post("/prestamo", status_code=201)
async def crear_prestamo(prestamo: Prestamo):
    query = text(f"SELECT * FROM Prestamos WHERE IDPrestamo={prestamo.IDPrestamo}")
    if db.execute(query).fetchone()!=None:
        raise HTTPException(status_code=204, detail="El prestamo ya existe")
    
    query = text(f"SELECT * FROM Libros WHERE IDLibro={prestamo.IDLibro}")
    
    if db.execute(query).fetchone()==None:
        raise HTTPException(status_code=204, detail="El libro no existe")
    
    query = text(f"INSERT INTO Prestamos (IDPrestamo, IDLibro, FechaPrestamo, FechaDevolucion) VALUES ({prestamo.IDPrestamo},{prestamo.IDLibro}, '{prestamo.FechaPrestamo}', '{prestamo.FechaDevolucion}')");
    db.execute(query)
    db.commit()
    db.close()
    
    return prestamo

@prestamo.get("/prestamos", response_model=List[Prestamo],status_code=200)
async def leer_prestamos():
    
    prestamos = db.query(PS).all()
    
    return prestamos

@prestamo.get("/prestamo/{IDPrestamo}", response_model=Prestamo, status_code=200)
async def leer_prestamo(IDPrestamo: int):
    prestamo = db.query(PS).filter(PS.IDPrestamo==IDPrestamo).first()
    
    if prestamo == None:
        raise HTTPException(status_code=204, detail="No se encontro prestamo")
    
    return prestamo

@prestamo.get("/prestamosAll", status_code=200)
async def leer_prestamos_all():
    prestamos_con_libros = db.query(LS, PS).join(PS, LS.IDLibro == PS.IDLibro)
    resultados_json = []
    for l, p in prestamos_con_libros:
        prestamo_info = {
            "IDPrestamo": p.IDPrestamo,
            "FechaPrestamo": p.FechaPrestamo,
            "Libro": {
                "IDLibro": l.IDLibro,
                "Titulo": l.Titulo,
                "Autor": l.Autor,
                "AnioPublicacion": l.AnioPublicacion
            }
        }
        resultados_json.append(prestamo_info)
    return resultados_json

@prestamo.put("/prestamo/{IDPrestamo}", status_code=200)
async def actualizar_prestamo(IDPrestamo: int, nuevoPrestamo: Prestamo):
    viejoPrestamo = db.query(PS).filter(PS.IDPrestamo==IDPrestamo).first()
    
    if viejoPrestamo:
        viejoPrestamo.IDPrestamo=nuevoPrestamo.IDPrestamo
        viejoPrestamo.IDLibro=nuevoPrestamo.IDLibro
        viejoPrestamo.FechaPrestamo=nuevoPrestamo.FechaPrestamo
        viejoPrestamo.FechaDevolucion=nuevoPrestamo.FechaDevolucion
        
        db.commit()
        return viejoPrestamo
    
    else:
        raise HTTPException(status_code=404, detail="No se pudo actualizar")
  
@prestamo.delete("/prestamo/{IDPrestamo}", response_model=Prestamo, status_code=200)
async def leer_prestamo(IDPrestamo: int):
    prestamo = db.query(PS).filter(PS.IDPrestamo==IDPrestamo).first()
    
    if prestamo:
        db.delete(prestamo)
        db.commit()
        return prestamo
    
    else:
        raise HTTPException(status_code=404, detail="No se pudo eliminar")