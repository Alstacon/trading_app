from datetime import datetime

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import MetaData, String, ForeignKey, JSON, Boolean
from sqlalchemy.orm import Mapped, mapped_column

from database import Base

metadata = MetaData()


class Role(Base):
    __tablename__ = 'role'
    metadata = metadata
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    permissions: Mapped[JSON] = mapped_column(nullable=True)


class User(SQLAlchemyBaseUserTable[int], Base):
    __tablename__ = 'user'
    metadata = metadata

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    registered_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)
    role_id: Mapped[int] = mapped_column(ForeignKey(Role.id))
    email: Mapped[str] = mapped_column(String(length=320), unique=True, index=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String(length=1024), nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    is_superuser: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    is_verified: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
