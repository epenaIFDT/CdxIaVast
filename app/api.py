from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
from pydantic import BaseModel
from .context_loader import load_knowledge
from .utils_search import buscar_info_rapida
import os

app = FastAPI()

# Centralización de rutas
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
FRONTEND_DIR = os.path.join(BASE_DIR, "frontend")
KNOWLEDGE_PATH = os.path.join(DATA_DIR, "vastec_knowledge.json")
FRONTEND_HTML = os.path.join(FRONTEND_DIR, "frontend.html")

class Consulta(BaseModel):
    pregunta: str

@app.on_event("startup")
def cargar_conocimiento():
    global knowledge
    knowledge = load_knowledge(KNOWLEDGE_PATH)



# Endpoint principal POST
@app.post("/consulta")
@app.post("/consulta/")
def consulta_post(data: Consulta):
    pregunta = data.pregunta.strip()
    if not pregunta:
        return {"respuesta": "Por favor, ingresa una pregunta válida."}
    respuesta = buscar_info_rapida(knowledge, pregunta)
    return {"respuesta": respuesta}


# Endpoint alternativo GET para pruebas rápidas
@app.get("/consulta")
@app.get("/consulta/")
def consulta_get(pregunta: str = ""):
    pregunta = pregunta.strip()
    if not pregunta:
        return {"respuesta": "Por favor, ingresa una pregunta válida."}
    respuesta = buscar_info_rapida(knowledge, pregunta)
    return {"respuesta": respuesta}


# Servir la interfaz web directamente
@app.get("/frontend.html")
def frontend():
    return FileResponse(FRONTEND_HTML)

@app.get("/")
def root():
    return FileResponse(FRONTEND_HTML)

