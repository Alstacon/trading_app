from datetime import datetime

from pydantic import BaseModel


class Base(BaseModel):
    class Config:
        '''Pydentic will convert to JSON even non-dict obj'''
        orm_mode = True


class OperationShow(Base):
    id: int
    quantity: str
    figi: str
    instrument_type: str
    date: datetime
    type: str


class OperationCreate(Base):
    id: int
    quantity: str
    figi: str
    instrument_type: str
    date: datetime
    type: str
