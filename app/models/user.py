from app.core.db import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Boolean, DateTime, text
from sqlalchemy.sql import func
from datetime import datetime


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    full_name: Mapped[str] = mapped_column(String(255), nullable=False)
    username: Mapped[str] = mapped_column(String(255), nullable=False, index=True)
    hashed_password: Mapped[str] = mapped_column(String(255), nullable=False)

    is_active: Mapped[bool] = mapped_column(
        Boolean, default=True, server_default=text("true"), nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )
    
    password_lst_updated: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=True)
