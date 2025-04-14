from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app import schemas, services 

router = APIRouter(tags=["Reservations"])


@router.get("/", response_model=list[schemas.Reservation])
def get_reservations(db: Session = Depends(get_db)):
    return services.get_all_reservations(db)


@router.post("/", response_model=schemas.Reservation)
def create_reservation(reservation: schemas.ReservationCreate, db: Session = Depends(get_db)):
    try:
        return services.create_reservation(db, reservation)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.delete("/{reservation_id}", response_model=schemas.Reservation)
def delete_reservation(reservation_id: int, db: Session = Depends(get_db)):
    reservation = services.delete_reservation(db, reservation_id)
    if not reservation:
        raise HTTPException(status_code=404, detail="Бронь не найдена")
    return reservation
