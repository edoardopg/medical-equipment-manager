from fastapi import FastAPI #importo libreria para la API
from crud.equipos import Equipos #importo el archivo equipos que contine CRUD
from pydantic import BaseModel #importo librería para recoger valores y hacer post y put
from crud.incidencias import Incidencias
from datetime import datetime,timedelta
from fastapi.middleware.cors import CORSMiddleware
from database import get_connection
import bcrypt
from jose import jwt


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class EquipoSchema(BaseModel): #creo clase Schema para recoger losd atos
    nombre: str
    tipo: str
    ubicacion: str

class IncidenciaSchema(BaseModel):
    id_equipo: int
    tipo_error: str
    descripcion: str

SECRET_KEY = "clave_secreta_muy_larga_y_segura"
ALGORITHM = "HS256"
class LoginSchema(BaseModel):
    username: str
    password: str

@app.post("/login")
def login(datos: LoginSchema):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM usuarios WHERE username=?''',(datos.username,))
    usuario = cursor.fetchone()
    conn.close()

    if usuario is None:
        return {"error": "Usuario no encontrado"}
    
    password_correcta = bcrypt.checkpw(
        datos.password.encode("utf-8"),
        usuario[2].encode("utf-8")
    )
    if not password_correcta:
        return {"error": "Contraseña inconrrecta"}
    
    token = jwt.encode(
        {"sub": datos.username, "exp": datetime.utcnow() + timedelta(hours=8)},
        SECRET_KEY,
        algorithm=ALGORITHM
    )
    return {"access_token": token}

@app.get("/") #ruta raíz de la API, devuelve un mensaje de bienvenida
def root():
    return {"mensaje": "API de equipos médicos funcionando"}

@app.get("/equipos")#ruta para obtener la lista de equipos médicos, devuelve un JSON con los datos de los equipos médicos almacenados en la base de datos
def get_equipos():
    equipos = Equipos()
    equipo = equipos.listar()
    return [
        {
            "id": e[0],
            "nombre": e[1],
            "tipo": e[2],
            "ubicacion": e[3]
        }
        for e in equipo
    ]
@app.get("/equipos/{id}")#ruta para obtener un equipo médico por su ID, devuelve un JSON con los datos del equipo médico correspondiente al ID proporcionado en la URL, si el equipo médico no existe devuelve un mensaje de error
def get_equipo(id:int):
    equipos = Equipos()
    equipo = equipos.buscar_por_id(id)
    if equipo is None:
        return {"error": "Equipo no encontrado"}
    return {
    "id": equipo[0],
    "nombre": equipo[1],
    "tipo": equipo[2],
    "ubicacion": equipo[3]
}

@app.post("/equipos")#ruta para crear un nuevo equipo médico, recibe un JSON con los datos del nuevo equipo médico a crear, si el equipo médico se crea correctamente devuelve un mensaje de éxito, si ocurre un error devuelve un mensaje de error
def crear_equipo(datos: EquipoSchema):
    equipos = Equipos()
    equipos.insertar(datos.nombre,datos.tipo,datos.ubicacion)
    return {"message":"Equipo creado correctamente"}

@app.put("/equipos/{id}")#ruta para actualizar un equipo médico por su ID, recibe un JSON con los datos actualizados del equipo médico, si el equipo médico se actualiza correctamente devuelve un mensaje de éxito, si el equipo médico no existe devuelve un mensaje de error 
def actualizar_equipo(id:int, datos: EquipoSchema):
    equipos = Equipos()
    equipo = equipos.buscar_por_id(id)
    if equipo is None:
        return {"error": "Equipo no encontrado"}
    equipos.actualizar(datos.nombre,datos.tipo,datos.ubicacion,id)
    return {"message": "Equipo actualizado correctamente"}

@app.delete("/equipos/{id}")#rduta para eliminar un equipo médico por su ID, si el equipo médico se elimina correctamente devuelve un mensaje de éxito, si el equipo médico no existe devuelve un mensaje de error
def eliminar_equipo(id:int):
    equipos = Equipos()
    equipo = equipos.buscar_por_id(id)
    if equipo is None:
        return {"error": "Equipo no encontrado"}        
    equipos.eliminar(id)
    return {"message":"Equipo eliminado correctamente"}

@app.get("/incidencias")
def get_incidencias():
    incidencias = Incidencias()
    incidencia = incidencias.listar()
    return [
        {
            "id_incidencia": i[0],
            "nombre_equipo": i[5],
            "tipo_error": i[3],
            "descripcion": i[4],
            "fecha": i[2],
            "id_equipo": i[1]
        }
        for i in incidencia
    ]

@app.get("/incidencias/{id}")
def get_incidencia(id:int):
    incidencias = Incidencias()
    incidencia = incidencias.buscar_por_id(id)
    if incidencia is None:
        return {"error": "Incidencia no encontrada"}
    return {
        "id_incidencia": incidencia[0],
        "nombre": incidencia[5],
        "tipo_error": incidencia[3],
        "descripcion": incidencia[4],
        "fecha": incidencia[2],
        "id_equipo": incidencia[1]
    }

@app.post("/incidencias")
def crear_incidencia(datos: IncidenciaSchema):
    equipos = Equipos()
    equipo = equipos.buscar_por_id(datos.id_equipo)
    if equipo is None:
        return {"error": "El equipo con ese ID no existe"}
    incidencias = Incidencias()
    fecha = datetime.now().strftime("%d/%m/%Y")
    incidencias.insertar(datos.id_equipo, fecha, datos.tipo_error, datos.descripcion)
    return {"message": "Incidencia creada correctamente"}

@app.put("/incidencias/{id}")
def actualizar_incidencia(id:int,datos:IncidenciaSchema):
    incidencias = Incidencias()
    incidencia = incidencias.buscar_por_id(id)
    if incidencia is None:
        return {"error": "Incidencia no encontrada"}
    fecha = datetime.now().strftime("%d/%m/%Y")
    incidencias.actualizar(fecha,datos.tipo_error,datos.descripcion,id)
    return {"message": "Incidencia actualizada"}

@app.delete("/incidencias/{id}")
def eliminar_incidencia(id:int):
    incidencias = Incidencias()
    incidencia = incidencias.buscar_por_id(id)
    if incidencia is None:
        return {"Error":"Incidencia no encontrada"}
    incidencias.eliminar(id)
    return {"message":"Incidencia eliminada correctamente"}
