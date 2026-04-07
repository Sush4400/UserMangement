from sqlalchemy.orm import Session
from app.models.user import User
from sqlalchemy import select
from app.core.security import hash_password



class UserDAO:

    @staticmethod
    def get_all(db: Session) -> list[User]:
        stmt = select(User)
        result = db.execute(stmt)
        return result.scalars().all()
    
    @staticmethod
    def get_by_id(db: Session, user_id: int) -> User:
        return db.get(User, user_id)
    
    @staticmethod
    def get_by_username(db: Session, username):
        stmt = select(User).where(User.username==username)
        result = db.execute(stmt)
        return result.scalar_one_or_none()
    
    @staticmethod
    def create(db: Session, user_data):
        user = User(
            full_name = user_data.full_name,
            username=user_data.username,
            hashed_password=hash_password(user_data.password)
        )
        db.add(user)
        db.commit()
        db.refresh(user)
        return user