from datetime import datetime

from sqlalchemy import MetaData
from sqlalchemy.orm import Mapped, mapped_column

from database import Base

metadata = MetaData()


class Operation(Base):
    __tablename__ = 'operation'
    metadata = metadata

    id: Mapped[int] = mapped_column(primary_key=True)
    quantity: Mapped[str]
    figi: Mapped[str]
    instrument_type: Mapped[str]
    date: Mapped[datetime] = mapped_column(default=datetime.utcnow)
    type: Mapped[str]
