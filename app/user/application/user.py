from fastapi import HTTPException
from user.domain.repositories.user_repositories import UserRepository
from user.domain.schemas.user_schema import UserSchema

class UserService:
    def __init__(self, repo: UserRepository):
        self.repo = repo

    def create_user(self, user: UserSchema):
        if self.repo.get_user_by_username(user.username):
            raise HTTPException(status_code=400, detail="Username already exists")
        if self.repo.get_user_by_email(user.email):
            raise  HTTPException(status_code=400, detail="Email already exists")
        return self.repo.create_user(user)

    def get_all_users(self):
        return self.repo.get_all_users()

    def get_user_by_id(self, user_id):
        if self.repo.get_user_by_id(user_id) == None:
            raise HTTPException(status_code=400, detail="User not exists")
        return self.repo.get_user_by_id(user_id)
    
    def update_user(self, user_id, user: UserSchema):
        if self.repo.get_user_by_id(user_id) == None:
            raise HTTPException(status_code=400, detail="User not exists")
        if self.repo.get_user_by_username(user.username):
            raise HTTPException(status_code=400, detail="Username already exists")
        if self.repo.get_user_by_email(user.email):
            raise  HTTPException(status_code=400, detail="Email already exists")
        return self.repo.update_user(user_id, user)
    
    def delete_user(self, user_id):
        if self.repo.get_user_by_id(user_id) == None:
            raise HTTPException(status_code=400, detail="User not exists")
        if self.repo.delete_user(user_id):
            return {"message": "User deleted successfully"}