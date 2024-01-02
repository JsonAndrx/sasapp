from abc import ABC, abstractmethod
from typing import List
from user.domain.schemas.user_schema import UserSchema

class UserRepository(ABC):
    @abstractmethod
    def create_user(self, user: UserSchema) -> UserSchema:
        pass

    @abstractmethod
    def get_user_by_username(self, username: str) -> bool:
        pass

    @abstractmethod
    def get_user_by_email(self, email: str) -> bool:
        pass

    @abstractmethod
    def get_all_users(self) -> List[UserSchema]:
        pass

    @abstractmethod
    def get_user_by_id(self, user_id: int) -> UserSchema:
        pass

    @abstractmethod
    def update_user(self, user_id: int, user: UserSchema) -> UserSchema:
        pass

    @abstractmethod
    def delete_user(self, user_id: int) -> bool:
        pass