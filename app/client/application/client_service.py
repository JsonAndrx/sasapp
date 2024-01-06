from fastapi import HTTPException
from client.domain.repositories.client_repositories import ClientRepository
from client.domain.schemas.client_schema import ClientSchema

class ClientService:
    def __init__(self, repo: ClientRepository):
        self.client_repo = repo

    def create_client(self, client: ClientSchema):
        if self.client_repo.get_client_by_num_document(client.num_document) and self.client_repo.get_client_by_phone(client.phone):
                raise HTTPException(status_code=400, detail="Client already exists")
        # if self.client_repo.get_client_by_phone(client.phone):
        #     raise  HTTPException(status_code=400, detail="Client already exists")
        return self.client_repo.create_client(client)
    
    def get_client_by_user(self, user_id):
        data = self.client_repo.get_client_by_user(user_id)
        print(data)
        if len(data) == 0:
            raise HTTPException(status_code=400, detail="You don't have a client")
        return self.client_repo.get_client_by_user(user_id)
    
    def update_client(self, client_id, client: ClientSchema):
        if self.client_repo.get_client_by_id(client_id) == None:
            raise HTTPException(status_code=400, detail="Client not exists")
        return self.client_repo.update_client(client_id, client)
    
    def delete_client(self, client_id):
        if self.client_repo.get_client_by_user(client_id) == None:
            raise HTTPException(status_code=400, detail="Client not exists")
        if self.client_repo.delete_client(client_id):
            return {"message": "Client deleted successfully"}
        
