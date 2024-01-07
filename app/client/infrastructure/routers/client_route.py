from fastapi import APIRouter
from client.domain.schemas.client_schema import ClientSchema, ClientSchemaOutput
from fastapi import Depends, HTTPException
from client.application.client_service import ClientService
from client.domain.repositories.client_repositories import ClientRepository

from client.infrastructure.repositories.client_repositories import ClientRepositoryDb
from user.application.authentication.auth_jwt import JWTUserBearer

from typing import List

router = APIRouter()

def get_client_service(
    client_repo: ClientRepository = Depends(ClientRepositoryDb)
) -> ClientService:
    return ClientService(client_repo)

def get_payload(payload: dict = Depends(JWTUserBearer())):
    return payload.get("id")

@router.post("/create", response_model=ClientSchemaOutput, dependencies=[Depends(JWTUserBearer())])
def create_client(client: ClientSchema, service: ClientService = Depends(get_client_service)):
    return service.create_client(client)

@router.get("/get_client_by_user", response_model=List[ClientSchemaOutput], dependencies=[Depends(JWTUserBearer())])
def get_client_by_user(user_id: int = Depends(get_payload), service: ClientService = Depends(get_client_service)):
    return service.get_client_by_user(user_id)

@router.put("/update_client/{client_id}", response_model=ClientSchemaOutput, dependencies=[Depends(JWTUserBearer())])
def update_client(client_id: int, client: ClientSchema, service: ClientService = Depends(get_client_service)):
    return service.update_client(client_id, client)

@router.delete("/delete_client/{client_id}", dependencies=[Depends(JWTUserBearer())])
def delete_client(client_id: int, service: ClientService = Depends(get_client_service)):
    return service.delete_client(client_id)