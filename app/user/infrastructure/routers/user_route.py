from fastapi import APIRouter
from user.domain.schemas.user_schema import UserSchema
from fastapi import Depends, HTTPException
from user.application.user import UserService
from user.domain.repositories.user_repositories import UserRepository
from business.domain.repositories.business_repositories import BusinessRepository

from user.infrastructure.repositories.user_repositories import UserRepositoryDb
from business.infrastructure.repositories.business_repositories import BusinessRepositoryDb
from user.application.authentication.auth_jwt import JWTAdminBearer
from typing import List

router = APIRouter()

def get_user_service(
    user_repo: UserRepository = Depends(UserRepositoryDb),
    business_repo: BusinessRepository = Depends(BusinessRepositoryDb)
) -> UserService:
    return UserService(user_repo, business_repo)

@router.post("/create", response_model=UserSchema, dependencies=[Depends(JWTAdminBearer())])
def create_user(user: UserSchema, service: UserService = Depends(get_user_service)):
    return service.create_user(user)

@router.get("/get_all_users", response_model=List[UserSchema], dependencies=[Depends(JWTAdminBearer())])  
def get_all_users(service: UserService = Depends(get_user_service)):
    try:
        return service.get_all_users()
    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=f"Error getting users {e}"
        )
    
@router.get("/get_user_by_id/{user_id}", response_model=UserSchema, dependencies=[Depends(JWTAdminBearer())])
def get_user_by_id(user_id: int, service: UserService = Depends(get_user_service)):
    return service.get_user_by_id(user_id)

@router.put("/update_user/{user_id}", response_model=UserSchema, dependencies=[Depends(JWTAdminBearer())])
def update_user(user_id: int, user: UserSchema, service: UserService = Depends(get_user_service)):
    return service.update_user(user_id, user)

@router.delete("/delete_user/{user_id}", dependencies=[Depends(JWTAdminBearer())])
def delete_user(user_id: int, service: UserService = Depends(get_user_service)):
    return service.delete_user(user_id)