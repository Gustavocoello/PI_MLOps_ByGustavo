from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import pandas as pd
import os
import uvicorn
# # proyecth-env\scripts\activate.bat (Activar el entorno virtual)
# uvicorn main:app --reload (Activar fastApi)
app = FastAPI()
   
df_games_items = pd.read_parquet('Playtime.parquet')

@app.get("/")
def index():
    return {"message": "Hello, world!"}

@app.get("/PlayTimeGenre/{genero}")
async def PlaytimeGenre(genero: str):
    result = df_games_items[df_games_items["genres"] == genero]

    # Encontrar el año con más horas jugadas para el género
    año_con_mas_horas = list(df_games_items[df_games_items["playtime"] == df_games_items["playtime"].max()]["release_year"])[0]
    return {f"Año de lanzamiento con más horas jugadas para {genero}": año_con_mas_horas}

