from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.schemas.user import UserResponse, UserCreate
from app.core.db import get_db
from app.services.user import UserService


router = APIRouter(prefix="/users", tags=['users'])

@router.get("", response_model=List[UserResponse])
def get_users(db: Session = Depends(get_db)):
    return UserService.get_users(db)


@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    return UserService.get_user(db, user_id)


@router.post("", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return UserService.create_user(db, user)