from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from user.application.authentication.jwt import decode_token

class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super().__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super().__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(status_code=403, detail="Invalid authentication")
            payload = self.verify_jwt(credentials.credentials)
            if not payload:
                raise HTTPException(status_code=403, detail="Invalid token")
            return payload
        else:
            raise HTTPException(status_code=403, detail="Invalid authorization code")
    
class JWTUserBearer(JWTBearer):
    def verify_jwt(self, jwtoken: str) -> dict:
        payload = None
        try:
            payload = decode_token(jwtoken)
        except:
            payload = None
        if payload:
            user_role = payload.get("role")
            if user_role != "user":
                raise HTTPException(status_code=403, detail="Invalid user role")
        return payload

class JWTAdminBearer(JWTBearer):
    def verify_jwt(self, jwtoken: str) -> bool:
        payload = None
        try:
            payload = decode_token(jwtoken)
        except:
            payload = None
        if payload:
            user_role = payload.get("role")
            if user_role != "admin":
                raise HTTPException(status_code=403, detail="Invalid user role")
        return payload