from abc import ABC, abstractmethod
from user.domain.schemas.auth_schema import RegisterSchema, LoginSchema

class AuthRepository(ABC):
    @abstractmethod
    def register_user(self, user: RegisterSchema) -> RegisterSchema:
        pass

    @abstractmethod
    def login_user(self, user: LoginSchema) -> LoginSchema:
        pass

    
    @abstractmethod
    def get_user_by_email(self, email: str) -> bool:
        pass

    @abstractmethod
    def get_user_by_username(self, username: str) -> bool:
        pass