from app.core.db import Base
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy.sql import func
from sqlalchemy import String, Boolean, ForeignKey, DateTime, DECIMAL, text
from datetime import datetime
from decimal import Decimal



class Book(Base):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String(255), nullable=False, index=True)
    price: Mapped[Decimal] = mapped_column(DECIMAL(10, 2), server_default=text("0.00"), nullable=False)
    author: Mapped[str] = mapped_column(String(255), nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, server_default=text('true'), default=True, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
