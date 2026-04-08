from app.core.config import get_settings
import bcrypt
from datetime import datetime, timezone, timedelta
from jose import jwt


settings = get_settings()


def hash_password(password: str) -> str:
    password_bytes = password.encode("utf-8")
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password_bytes, salt).decode()


def verify_password(password: str, hashed: str) -> bool:
    return bcrypt.checkpw(password.encode(), hashed.encode())

'''
def hash_password(password: str) -> str:
    # password.encode("utf-8"): Convert string to bytes
    # sha256: converts password into fixed 32-byte hash
    #digest: gives that hash in raw bytes
    password_bytes = hashlib.sha256(password.encode("utf-8")).digest()

    # A salt is a random value added to the password before hashing
    salt = bcrypt.gensalt()

    # Final hashing: Combines: password + salt + cost → final hash
    return bcrypt.hashpw(password_bytes, salt).decode()


def verify_password(password: str, hashed: str) -> bool:
    password_bytes = hashlib.sha256(password.encode("utf-8")).digest()
    return bcrypt.checkpw(password_bytes, hashed.encode())


What is SHA-256?
SHA-256 is a cryptographic hash function (from the SHA-2 family).
It takes any input and produces a fixed 256-bit (32-byte) output
'''

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    result = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return result


def decode_token(token: str):
    return jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])