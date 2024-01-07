from fastapi import HTTPException
from user.domain.repositories.auth_repositories import AuthRepository
from user.domain.schemas.auth_schema import RegisterSchema, LoginSchema
from user.application.authentication.jwt import create_token

class AuthServices:
    def __init__(self, repo: AuthRepository):
        self.repo = repo

    def register_user(self, user: RegisterSchema):
        if self.repo.get_user_by_username(user.username):
            raise HTTPException(status_code=400, detail="Username already exists")
        if self.repo.get_user_by_email(user.email):
            raise  HTTPException(status_code=400, detail="Email already exists")
        return self.repo.register_user(user)
    
    def login_user(self, user: LoginSchema):
        user_data = self.repo.login_user(user.username, user.password)
        if user_data == None:
            raise HTTPException(status_code=400, detail="User not exists")
        response = create_token({"username": user_data.username, "id": user_data.id, "role": user_data.role})
        return {"username": user.username, "token": response}