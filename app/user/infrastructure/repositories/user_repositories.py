from sqlalchemy.orm import Session
from user.domain.models.user_model import UserModel
from user.domain.repositories.user_repositories import UserRepository
from config.database.connection import SessionLocal, get_db
from fastapi import Depends, status, HTTPException
import traceback
from datetime import date


class UserRepositoryDb(UserRepository):
    def __init__(self, session: Session = Depends(get_db)):
        self.session = session
    
    def get_all_users(self):
        try:
            db = SessionLocal()
            users = db.query(UserModel).all()
            return users
        except Exception as e:
            raise Exception(
                status_code = status.HTTP_409_NOT_FOUND,
                detail = f"Error getting users {e}"
            )
    
    def create_user(self, user):
        try:
            db_user = UserModel(**user.dict())
            self.session.add(db_user)
            self.session.commit()
            self.session.refresh(db_user)
            return db_user
        except Exception as e:
            print(e)
            traceback.print_exc()
            raise HTTPException(
                status_code = status.HTTP_409_CONFLICT,
                detail = f"Error creating user {e}"
            )
        
    def get_user_by_id(self, user_id):
        try:
            user = self.session.query(UserModel).filter(UserModel.id == user_id).first()
            return user
        except Exception as e:
            raise HTTPException(
                status_code = status.HTTP_409_CONFLICT,
                detail = f"Error getting user {e}"
            )
        
    def update_user(self, user_id, user):
        try:
            db_user = self.session.query(UserModel).filter(UserModel.id == user_id).first()
            db_user.name = user.name
            db_user.email = user.email
            self.session.commit()
            self.session.refresh(db_user)
            return db_user
        except Exception as e:
            raise HTTPException(
                status_code = status.HTTP_409_CONFLICT,
                detail = f"Error updating user {e}"
            )
        
    def delete_user(self, user_id):
        try:
            db_user = self.session.query(UserModel).filter(UserModel.id == user_id).first()
            self.session.delete(db_user)
            self.session.commit()
            return db_user
        except Exception as e:
            raise HTTPException(
                status_code = status.HTTP_409_CONFLICT,
                detail = f"Error deleting user {e}"
            )
    
    def get_user_by_email(self, email):
        try:
            user = self.session.query(UserModel).filter(UserModel.email == email).first()
            return user
        except Exception as e:
            raise HTTPException(
                status_code = status.HTTP_409_CONFLICT,
                detail = f"Error getting user {e}"
            )
        
    def get_user_by_username(self, username):
        try:
            user = self.session.query(UserModel).filter(UserModel.username == username).first()
            return user
        except Exception as e:
            raise HTTPException(
                status_code = status.HTTP_409_CONFLICT,
                detail = f"Error getting user {e}"
            )
        

        