from abc import ABC, abstractmethod
from typing import List
from client.domain.schemas.client_schema import ClientSchema

class ClientRepository(ABC):
    @abstractmethod
    def create_client(self, client: ClientSchema) -> ClientSchema:
        pass

    @abstractmethod
    def get_client_by_user(self, user_id: int) -> List[ClientSchema]:
        pass

    @abstractmethod
    def get_client_by_id(self, client_id: int) -> ClientSchema:
        pass
    
    # @abstractmethod
    # def get_all_clients(self) -> List[ClientSchema]:
    #     pass

    @abstractmethod
    def update_client(self, client_id: int, client: ClientSchema) -> ClientSchema:
        pass

    @abstractmethod
    def delete_client(self, client_id: int) -> bool:
        pass

    @abstractmethod
    def get_client_by_num_document(self, num_document: str) -> bool:
        pass

    @abstractmethod
    def get_client_by_phone(self, phone: str) -> bool:
        pass