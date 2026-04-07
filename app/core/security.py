from app.core.config import get_settings
import bcrypt, hashlib


settings = get_settings()


def hash_password(password: str) -> str:
    password_bytes = hashlib.sha256(password.encode("utf-8")).digest()
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password_bytes, salt).decode()
