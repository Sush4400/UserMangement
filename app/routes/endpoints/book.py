from fastapi import APIRouter, Depends
from typing import List
from app.schemas.book import BookResponse
from sqlalchemy.orm import Session
from app.core.db import get_db



router = APIRouter(prefix="/books", tags=["books"])


# @router.get("", response_model=List[BookResponse])
# def get_books(db: Session = Depends(get_db())):
#     pass