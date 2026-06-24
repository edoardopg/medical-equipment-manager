from fastapi import APIRouter, Depends
from routers.users import verify_token
from pydantic import BaseModel
from crud.equipments import Equipments

router = APIRouter()

class EquipmentSchema(BaseModel): #creo clase Schema para recoger los datos
    name: str
    type: str
    location: str

@router.get("/equipments")#ruta para obtener la lista de equipos médicos, devuelve un JSON con los datos de los equipos médicos almacenados en la base de datos
def get_equipments(current_user=Depends(verify_token)):
    equipments = Equipments()
    equipment = equipments.list()
    return [
        {
            "id": e[0],
            "name": e[1],
            "type": e[2],
            "location": e[3]
        }
        for e in equipment
    ]

@router.get("/equipments/{id}")#ruta para obtener un equipo médico por su ID, devuelve un JSON con los datos del equipo médico correspondiente al ID proporcionado en la URL, si el equipo médico no existe devuelve un mensaje de error
def get_equipment(id:int,current_user=Depends(verify_token)):
    equipments = Equipments()
    equipment = equipments.find_by_id(id)
    if equipment is None:
        return {"error": "Equipment not found"}
    return {
    "id": equipment[0],
    "name": equipment[1],
    "type": equipment[2],
    "location": equipment[3]
}

@router.post("/equipments")#ruta para crear un nuevo equipo médico, recibe un JSON con los datos del nuevo equipo médico a crear, si el equipo médico se crea correctamente devuelve un mensaje de éxito, si ocurre un error devuelve un mensaje de error
def create_equipment(data: EquipmentSchema,current_user=Depends(verify_token)):
    equipments = Equipments()
    equipments.insert(data.name,data.type,data.location)
    return {"message":"Equipment create successfully"}

@router.put("/equipments/{id}")#ruta para actualizar un equipo médico por su ID, recibe un JSON con los datos actualizados del equipo médico, si el equipo médico se actualiza correctamente devuelve un mensaje de éxito, si el equipo médico no existe devuelve un mensaje de error 
def update_equipment(id:int, data: EquipmentSchema,current_user=Depends(verify_token)):
    equipments = Equipments()
    equipment = equipments.find_by_id(id)
    if equipment is None:
        return {"error": "Equipment not found"}
    equipments.update(data.name,data.type,data.location,id)
    return {"message": "Equipment update successfullly"}

@router.delete("/equipments/{id}")#ruta para eliminar un equipo médico por su ID, si el equipo médico se elimina correctamente devuelve un mensaje de éxito, si el equipo médico no existe devuelve un mensaje de error
def delete_equipment(id:int,current_user=Depends(verify_token)):
    equipments = Equipments()
    equipment = equipments.find_by_id(id)
    if equipment is None:
        return {"error": "Equipment not found"}        
    equipments.delete(id)
    return {"message":"Equipment delete successfully"}
