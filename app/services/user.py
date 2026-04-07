from sqlalchemy.orm import Session
from app.crud.user import UserDAO
from fastapi import HTTPException



class UserService:

    @staticmethod
    def get_users(db: Session):
        return UserDAO.get_all(db)
    
    @staticmethod
    def get_user(db: Session, user_id: int):
        user = UserDAO.get_by_id(db, user_id)
        if not user:
            raise HTTPException(404, "User not found !!")
        return user
    
    @staticmethod
    def create_user(db: Session, user_data):
        existing = UserDAO.get_by_username(db, user_data.username)
        if existing:
            raise HTTPException(400, "Username already exists !")
        return UserDAO.create(db, user_data)