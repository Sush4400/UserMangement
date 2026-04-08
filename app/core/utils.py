from fastapi import Depends
from fastapi.security import HTTPBearer
from .security import decode_token



security = HTTPBearer()

def get_current_user(token=Depends(security)):
    token_str = token.credentials
    payload = decode_token(token_str)
    return payload['sub']