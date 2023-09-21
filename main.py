from fastapi import FastAPI
from routers import libro
from routers import prestamo

app = FastAPI()
# Routers
app.include_router(libro.libro)
app.include_router(prestamo.prestamo)