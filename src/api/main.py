from fastapi import FastAPI

from src.api.routers.vehiculos import router as vehiculo_router
from src.api.routers.clientes import router as cliente_router
from src.api.routers.alquileres import router as alquiler_router

app = FastAPI(
    title="API Rent System"
)


@app.get("/")
def home():
    return {"mensaje": "Bienvenido a API Rent System"}


app.include_router(vehiculo_router)
app.include_router(cliente_router)
app.include_router(alquiler_router)
