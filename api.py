from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import equipments,incidents,users
from models import create_table,insert_initial_data,create_admin

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

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

