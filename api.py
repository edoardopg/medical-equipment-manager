from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import equipments,incidents,users
from models import create_table,insert_initial_data,create_admin
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os 


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(equipments.router)
app.include_router(incidents.router)
app.include_router(users.router)

@app.on_event("startup")
def startup_event():
    create_table()
    insert_initial_data()
    create_admin()

# Servir frontend como SPA (Single Page Application)
if os.path.exists("frontend"):
    @app.get("/{full_path:path}")
    def serve_frontend(full_path: str):
        # Si es una ruta de la API, no la sirvas como frontend
        if full_path.startswith("api") or full_path.startswith("equipments") or full_path.startswith("incidents") or full_path.startswith("register") or full_path.startswith("login") or full_path.startswith("forgot") or full_path.startswith("reset"):
            return {"error": "not found"}
        # Si no, sirve el index.html (el frontend maneja la navegación)
        return FileResponse("frontend/index.html")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

