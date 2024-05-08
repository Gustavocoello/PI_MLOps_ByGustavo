from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import pandas as pd
import os

# # proyecth-env\scripts\activate.bat (Activar el entorno virtual)
# uvicorn main:app --reload (Activar fastApi)
app = FastAPI()
   

# Obtener la ruta del directorio actual
current_dir = os.path.dirname(__file__)
# Ruta completa del archivo
file_path = os.path.join(current_dir, "Playtime.parquet")
# Lectura de datos 
df_games_items = pd.read_parquet(file_path)


@app.get("/")
def index():
    return {"message": "Hello, world!"}

@app.get("/PlayTimeGenre/{genero}")
async def PlaytimeGenre(genero: str):
    filtro = df_games_items[df_games_items['genres'] == genero]
    group = filtro[filtro['playtime_forever'] == filtro['playtime_forever'].max()]
    max_year = group['Year'].values[0]
    return {"Año de lanzamiento con más horas jugadas para Género " + genero: max_year}