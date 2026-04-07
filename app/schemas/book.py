from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime
from decimal import Decimal



class BookBase(BaseModel):
    title: str
    price: Decimal
    author: str
    is_active: bool


class BookCreate(BookBase):
    pass


class BookUpdate(BaseModel):
    title: Optional[str] = None
    price: Optional[Decimal] = 0.00
    author: Optional[str] = None
    is_active: Optional[bool] = None


class BookResponse(BookBase):
    id: str
    created_at: datetime
    updated_at: datetime
    model_config = ConfigDict(
        from_attributes=True,
        json_encoders={
            datetime: lambda x: x.strftime("%Y-%m-%d %H:%M%S") if x else None
        }
    )