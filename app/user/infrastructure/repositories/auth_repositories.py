from sqlalchemy.orm import Session
from user.domain.models.user_model import UserModel
from user.domain.repositories.auth_repositories import AuthRepository
from fastapi import Depends, status, HTTPException
from config.database.connection import SessionLocal, get_db
from user.application.authentication.hashing import hash_password, verify_password
from datetime import date

class AuthRepositoryDb(AuthRepository):
    def __init__(self, session: Session = Depends(get_db)):
        self.session = session

    def login_user(self, username, password):
        user = self.session.query(UserModel).filter(
            UserModel.username == username
        ).first()
        if user and verify_password(password, user.password):
            return user
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
            )

        
    def register_user(self, user):
        try:
            user.created_at = date.today()
            user.is_active = 0
            user.password = hash_password(user.password)
            print(user.password)
            db_user = UserModel(**user.dict())
            self.session.add(db_user)
            self.session.commit()
            self.session.refresh(db_user)
            return db_user
        except Exception as e:
            raise HTTPException(
                status_code = status.HTTP_409_CONFLICT,
                detail = f"Error register user {e}")
        
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