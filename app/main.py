from fastapi import FastAPI
from app.database import engine, Base
from app.routers import tables, reservations

app = FastAPI()

app.include_router(tables.router, prefix="/tables", tags=["Tables"])
app.include_router(reservations.router, prefix="/reservations", tags=["Reservations"])

@app.get("/")
def read_root():
    return {"message": "123"}
