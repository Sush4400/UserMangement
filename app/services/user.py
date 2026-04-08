from sqlalchemy.orm import Session
from app.crud.user import UserDAO
from fastapi import HTTPException
from app.core.security import *



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
    

    @staticmethod
    def update_user(db: Session, user_id: int, data: dict):
        user = UserDAO.get_by_id(db, user_id)
        if not user:
            raise HTTPException(404, "User not found !")
        return UserDAO.update(db, user, data)
    

    @staticmethod
    def delete_user(db: Session, user_id: int):
        result = UserDAO.delete(db, user_id)
        if result.rowcount == 0:
            raise HTTPException(404, "User not found")
        else:
            return {"status": True, "detail": "User deleted successfully."}
        

    @staticmethod
    def login_user(db: Session, data: dict):
        user = UserDAO.get_by_username(db, data.username)
        if not user or not verify_password(data.password, user.hashed_password):
            raise HTTPException(401, "Invalid credentials!")
        token = create_access_token({"sub": str(user.id)})
        return {"access_token": token, "token_type": "bearer"}
    

    @staticmethod
    def change_password(db: Session, data, user_id):
        user = UserDAO.get_by_id(db, user_id)
        if not user:
            raise HTTPException(404, "User not found")
        if not verify_password(data.old_password, user.hashed_password):
            raise HTTPException(400, "Wrong old password")
        hashed = hash_password(data.new_password)
        curr_date = datetime.now()
        print("curr date: ", curr_date)
        return
        return UserDAO.change_password(db, user, hashed)