from datetime import datetime

from sqlalchemy import MetaData, String, TIMESTAMP, ForeignKey, JSON, Boolean
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

metadata = MetaData()


class Base(DeclarativeBase):
    type_annotation_map = {
        JSON: JSON,
        datetime: TIMESTAMP(timezone=True),
    }


class Role(Base):
    __tablename__ = 'role'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    permissions: Mapped[JSON] = mapped_column(nullable=True)


class User(Base):
    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    registered_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)
    role_id: Mapped[int] = mapped_column(ForeignKey(Role.id))
    email: Mapped[str] = mapped_column(String(length=320), unique=True, index=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String(length=1024), nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    is_superuser: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    is_verified: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
