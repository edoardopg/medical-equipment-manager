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
# Servir frontend estático
if os.path.exists("frontend"):
    app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

