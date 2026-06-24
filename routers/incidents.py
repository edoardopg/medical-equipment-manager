from fastapi import APIRouter,Depends
from routers.users import verify_token
from pydantic import BaseModel
from crud.incidents import Incidents
from datetime import datetime 

router = APIRouter()

class IncidentSchema(BaseModel):
    id_equipment: int
    type_error: str
    description: str


@router.get("/incidents") #ruta para obtener la lista de incidencias
def get_incidents(current_user=Depends(verify_token)):
    incidents = Incidents()
    incident = incidents.list()
    return[
        {
            "id_incident": i[0],
            "equipment_name": i[5],
            "id_equipment": i[1],
            "date": i[2],
            "type_error": i[3],
            "description": i[4],
        }
        for i in incident
    ]

@router.get("/incidents/{id}")
def get_incident_id(id:int, current_user=Depends(verify_token)):
    incidents = Incidents()
    incident = incidents.find_by_id(id)
    if incident is None:
        return{"error": "Incident not found"}
    return{
            "id_incident": incident[0],
            "equipment_name": incident[5],
            "id_equipment": incident[1],
            "date": incident[2],
            "type_error": incident[3],
            "description": incident[4],
    }

@router.post("/incidents") #ruta para crear una nueva incidencia, recibe un JSON con los datos de la nueva incidencia, si se crea correctamente devuelve un mensaje de éxito, si da error devuelve un mensaje de error
def post_incident(data: IncidentSchema, current_user=Depends(verify_token)):
    incidents = Incidents()
    date = datetime.now().strftime("%Y-%m-%d")
    incidents.insert(data.id_equipment,date,data.type_error,data.description)
    return {"message": "Incident create successfully"}

@router.delete("/incidents/{id}") #ruta para eliminar una incidencia,busca la incidencia por su id, si la encuentra la borra sino manda un mensaje de error (not found)
def delete_incident(id:int,current_user=Depends(verify_token)):
    incidents = Incidents()
    incident = incidents.find_by_id(id)
    if incident is None:
        return {"error": "incident not found"}
    incidents.delete(id)
    return {"message": "incident delete successfully"}

@router.put("/incidents/{id}") #ruta para actualizar una incidencia, busca la incidencia por id, recibe un JSON  con los datos nuevos de la incidencia, manda mensaje si se actualiza correctamente y de error si no encuentra la incidencia
def update_incident(id:int,data: IncidentSchema, current_user=Depends(verify_token)):
    incidents = Incidents()
    incident = incidents.find_by_id(id)
    if incident is None:
        return {"error": "incident not found"}
    date = datetime.now().strftime("%Y-%m-%d")
    incidents.update(date,data.type_error,data.description,id)
    return {"message": "incident update successfully"}