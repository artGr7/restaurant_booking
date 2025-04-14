from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Table(Base):
    __tablename__ = "tables"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    seats = Column(Integer, nullable=False)
    location = Column(String, nullable=False)
    reservations = relationship("Reservation", back_populates="table")

class Reservation(Base):
    __tablename__ = "reservations"

    id = Column(Integer, primary_key=True, index=True)
    table_id = Column(Integer, ForeignKey("tables.id"), nullable=False)
    customer_name = Column(String, nullable=False)
    duration_minutes = Column(Integer, nullable=False)
    reserved_time = Column(DateTime, nullable=False)

    table = relationship("Table", back_populates="reservations")
