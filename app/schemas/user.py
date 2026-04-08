from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime



class UserBase(BaseModel):
    full_name: str
    username: str


class UserCreate(UserBase):
    password: str


class UserUpdate(BaseModel):
    full_name: Optional[str] = None
    is_active: Optional[bool] = None


class UserResponse(UserBase):
    id: int
    is_active: bool
    created_at: datetime
    updated_at: datetime
    model_config = ConfigDict(
        from_attributes=True,
        json_encoders={
            datetime: lambda v: v.strftime("%Y-%m-%d %H:%M:%S") if v else None
        }
    )
 

class UserLogin(BaseModel):
    username: str
    password: str


class UserResetPassword(BaseModel):
    old_password: str
    new_password: str
