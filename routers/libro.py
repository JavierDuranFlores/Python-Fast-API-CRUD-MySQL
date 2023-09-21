from fastapi import APIRouter, status, HTTPException
from config.db import SessionLocal
from schemas.libros import Libro
from sqlalchemy import text
from typing import List
from models.libro import Libro as LS
libro = APIRouter()

db = SessionLocal()


@libro.post("/libro", response_model=Libro,status_code=201)
async def crear_libro(libro: Libro):
    
    query = text(f"SELECT * FROM Libros WHERE IDLibro = {libro.IDLibro}")
    
    result = db.execute(query).fetchone()
    
    if result!=None:
        raise HTTPException(status_code=204, detail="El libro ya existe")
    
    
    query = text(f"INSERT INTO Libros (IDLibro, Titulo, Autor, AnioPublicacion) VALUES ({libro.IDLibro}, '{libro.Titulo}', '{libro.Autor}', {libro.AnioPublicacion})")
    db.execute(query)
    db.commit()
    db.close()
    
    return libro


@libro.get("/libro/{IDLibro}", response_model=Libro, status_code=200)
async def buscar_libro(IDLibro: int):
    
    query = text(f"SELECT * FROM Libros WHERE IDLibro = {IDLibro};")
    
    resultado = db.execute(query)
    
    libro = resultado.fetchone()
    
    db.close()
    
    return libro

@libro.get("/libro", response_model=List[Libro], status_code=200)
async def leer_libros():
        
    libros = db.query(LS).all()

    return libros

@libro.put("/libro/{IDLibro}", response_model=Libro, status_code=status.HTTP_200_OK)    
async def actualizar_libro(IDLibro: int, libro: Libro):
    query = text(f"UPDATE Libros SET Titulo='{libro.Titulo}', Autor='{libro.Autor}', AnioPublicacion={libro.AnioPublicacion} WHERE IDLibro = {IDLibro}");
    
    db.execute(query)
        
    db.commit()
    db.close()
    
    libro.IDLibro = IDLibro
    
    return libro
    
@libro.delete("/libro/{IDLibro}", response_model=[], status_code=200)
async def eliminar_libro(IDLibro: int):
    query = text(f"DELETE FROM Libros WHERE IDLibro = {IDLibro}")
    
    db.execute(query)
    
    db.commit()
    db.close()
    
    return {"id": IDLibro}