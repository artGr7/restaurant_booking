from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app import schemas, services

router = APIRouter(tags=["Tables"])


@router.get("/", response_model=list[schemas.Table])
def get_tables(db: Session = Depends(get_db)):
    return services.get_all_tables(db)


@router.post("/", response_model=schemas.Table)
def create_table(table: schemas.TableCreate, db: Session = Depends(get_db)):
    return services.create_table(db, table)


@router.delete("/{table_id}", response_model=schemas.Table)
def delete_table(table_id: int, db: Session = Depends(get_db)):
    table = services.delete_table(db, table_id)
    if not table:
        raise HTTPException(status_code=404, detail="Столик не найден")
    return table
