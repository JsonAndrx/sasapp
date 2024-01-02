from fastapi import APIRouter
from fastapi import Depends, HTTPException
from user.domain.schemas.auth_schema import RegisterSchema, LoginSchema, LoginSchemaOut, RegisterSchemaOutput
from user.domain.repositories.auth_repositories import AuthRepository

from user.infrastructure.repositories.auth_repositories import AuthRepositoryDb
from user.application.auth import AuthServices

router = APIRouter()

def get_auth_service(repo: AuthRepository = Depends(AuthRepositoryDb)) -> AuthServices:
    return AuthServices(repo)

@router.post("/register", response_model=RegisterSchemaOutput)
def register_user(user: RegisterSchema, service: AuthServices = Depends(get_auth_service)):
    return service.register_user(user)

@router.post("/login", response_model=LoginSchemaOut)
def login_user(user: LoginSchema, service: AuthServices = Depends(get_auth_service)):
    return service.login_user(user)