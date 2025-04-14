from sqlalchemy.orm import Session
from app import models, schemas
from datetime import timedelta
import logging
logger = logging.getLogger(__name__)


# tables

def get_all_tables(db: Session):
    return db.query(models.Table).all()

def create_table(db: Session, table: schemas.TableCreate):
    db_table = models.Table(**table.model_dump())
    db.add(db_table)
    db.commit()
    db.refresh(db_table)
    logger.info(f"Создан новый стол: {db_table}")
    return db_table

def delete_table(db: Session, table_id: int):
    table = db.query(models.Table).filter(models.Table.id == table_id).first()
    if table:
        db.delete(table)
        db.commit()
        logger.info(f"Удалён стол: {table}")
    else:
        logger.warning(f"Стол с id {table_id} не найден.")
    return table

# reservations 

def get_all_reservations(db: Session):
    return db.query(models.Reservation).all()

def create_reservation(db: Session, reservation: schemas.ReservationCreate):
    start_time = reservation.reserved_time.replace(tzinfo=None)
    end_time = start_time + timedelta(minutes=reservation.duration_minutes)

    existing_reservations = db.query(models.Reservation).filter(
        models.Reservation.table_id == reservation.table_id,
        models.Reservation.reserved_time < end_time
    ).all()

    for existing in existing_reservations:
        existing_end = existing.reserved_time + timedelta(minutes=existing.duration_minutes)
        if existing_end > start_time:
            logger.warning(
                f"Конфликт с существующей бронью: стол #{existing.table_id}, "
                f"с {existing.reserved_time} до {existing_end}"
            )
            raise ValueError("Это время уже занято для выбранного стола.")

    db_reservation = models.Reservation(**reservation.model_dump())
    db.add(db_reservation)
    db.commit()
    db.refresh(db_reservation)
    logger.info(f"Бронь успешно создана: {db_reservation}")
    return db_reservation



def delete_reservation(db: Session, reservation_id: int):
    reservation = db.query(models.Reservation).filter(models.Reservation.id == reservation_id).first()
    if reservation:
        db.delete(reservation)
        db.commit()
        logger.info(f"Удалена бронь: {reservation}")
    return reservation
