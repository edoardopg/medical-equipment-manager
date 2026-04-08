from fastapi import FastAPI #importo libreria para la API
from crud.equipos import Equipos #importo el archivo equipos que contine CRUD
from pydantic import BaseModel #importo librería para recoger valores y hacer post y put

app = FastAPI()
class EquipoSchema(BaseModel): #creo clase Schema para recoger losd atos
    nombre: str
    tipo: str
    ubicacion: str

@app.get("/") #ruta raíz de la API, devuelve un mensaje de bienvenida
def root():
    return {"mensaje": "API de equipos médicos funcionando"}

@app.get("/equipos")#ruta para obtener la lista de equipos médicos, devuelve un JSON con los datos de los equipos médicos almacenados en la base de datos
def get_equipos():
    equipo = Equipos()
    equipos = equipo.listar()
    return [
        {
            "id": e[0],
            "nombre": e[1],
            "tipo": e[2],
            "ubicacion": e[3]
        }
        for e in equipos
    ]
@app.get("/equipos/{id}")#ruta para obtener un equipo médico por su ID, devuelve un JSON con los datos del equipo médico correspondiente al ID proporcionado en la URL, si el equipo médico no existe devuelve un mensaje de error
def get_equipo(id:int):
    equipos = Equipos()
    e = equipos.buscar_por_id(id)
    if e is None:
        return {"error": "Equipo no encontrado"}
    return {
    "id": e[0],
    "nombre": e[1],
    "tipo": e[2],
    "ubicacion": e[3]
}

@app.post("/equipos")#ruta para crear un nuevo equipo médico, recibe un JSON con los datos del nuevo equipo médico a crear, si el equipo médico se crea correctamente devuelve un mensaje de éxito, si ocurre un error devuelve un mensaje de error
def crear_equipo(datos: EquipoSchema):
    equipo = Equipos()
    equipo.insertar(datos.nombre,datos.tipo,datos.ubicacion)
    return {"message":"Equipo creado correctamente"}

@app.put("/equipos/{id}")#ruta para actualizar un equipo médico por su ID, recibe un JSON con los datos actualizados del equipo médico, si el equipo médico se actualiza correctamente devuelve un mensaje de éxito, si el equipo médico no existe devuelve un mensaje de error 
def actualizar_equipo(id:int, datos: EquipoSchema):
    equipo = Equipos()
    e = equipo.buscar_por_id(id)
    if e is None:
        return {"error": "Equipo no encontrado"}
    equipo.actualizar(datos.nombre,datos.tipo,datos.ubicacion,id)
    return {"message": "Equipo actualizado correctamente"}

@app.delete("/equipos/{id}")#rduta para eliminar un equipo médico por su ID, si el equipo médico se elimina correctamente devuelve un mensaje de éxito, si el equipo médico no existe devuelve un mensaje de error
def eliminar_equipo(id:int):
    equipo = Equipos()
    e = equipo.buscar_por_id(id)
    if e is None:
        return {"error": "Equipo no encontrado"}        
    equipo.eliminar(id)
    return {"message":"Equipo eliminado correctamente"}