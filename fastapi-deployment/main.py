from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

# # proyecth-env\scripts\activate.bat (Activar el entorno virtual)
# uvicorn main:app --reload (Activar fastApi)
app = FastAPI()


class Libro(BaseModel):
    titulo: str
    autor: str
    paginas: int
    editorial: Optional[str]
    


@app.get("/")
def index():
    return {"message" : "Hola mundo"}

@app.get("/Libros/{id}")
def mostrar_libro(id: int):
    return {"data": id}

@app.post("/Libros")
def insert_libro(libro: Libro):
    return {"message": f"libro {libro.titulo} insertado"}