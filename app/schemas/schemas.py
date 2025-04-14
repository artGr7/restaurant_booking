from datetime import datetime
from pydantic import BaseModel

class TableBase(BaseModel):
    name: str
    seats: int
    location: str

class TableCreate(TableBase):
    pass

class Table(TableBase):
    id: int

    model_config = {
        "from_attributes": True
    }

class ReservationBase(BaseModel):
    table_id: int
    customer_name: str
    duration_minutes: int
    reserved_time: datetime

class ReservationCreate(ReservationBase):
    pass

class Reservation(ReservationBase):
    id: int

    model_config = {
        "from_attributes": True
    }
