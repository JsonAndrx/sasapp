from sqlalchemy.orm import Session
from client.domain.schemas.client_schema import ClientSchema
from client.domain.models.client_model import ClientModel
from client.domain.repositories.client_repositories import ClientRepository
from config.database.connection import SessionLocal, get_db
from fastapi import Depends, status, HTTPException

class ClientRepositoryDb(ClientRepository):
    def __init__(self, session: Session = Depends(get_db)):
        self.session = session

    def create_client(self, client):
        try:
            db_client = ClientModel(**client.dict())
            self.session.add(db_client)
            self.session.commit()
            self.session.refresh(db_client)
            return db_client
        except Exception as e:
            raise HTTPException(
                status_code = status.HTTP_409_CONFLICT,
                detail = f"Error creating client {e}"
            )
        
    def update_client(self, client_id, client):
        try:
            db_client = self.session.query(ClientModel).filter(ClientModel.id == client_id).first()
            db_client.first_name = client.first_name
            db_client.last_name = client.last_name
            db_client.dob = client.dob
            db_client.type_document = client.type_document
            db_client.num_document = client.num_document
            db_client.phone = client.phone
            db_client.email = client.email
            db_client.address = client.address
            self.session.commit()
            self.session.refresh(db_client)
            return db_client
        except Exception as e:
            raise HTTPException(
                status_code = status.HTTP_409_CONFLICT,
                detail = f"Error updating client {e}"
            )

    def get_client_by_user(self, user_id):
        try:
            client = self.session.query(ClientModel).filter(ClientModel.id_username == user_id).all()
            
            return client
        except Exception as e:
            raise HTTPException(
                status_code = status.HTTP_409_CONFLICT,
                detail = f"Error getting client {e}"
            )
        
    def get_client_by_id(self, client_id):
        try:
            client = self.session.query(ClientModel).filter(ClientModel.id == client_id).first()
            return client
        except Exception as e:
            raise HTTPException(
                status_code = status.HTTP_409_CONFLICT,
                detail = f"Error getting client {e}"
            )
        
    def get_client_by_num_document(self, num_document: str):
        try:
            client = self.session.query(ClientModel).filter(ClientModel.num_document == num_document).first()
            return client
        except Exception as e:
            raise HTTPException(
                status_code = status.HTTP_409_CONFLICT,
                detail = f"Error getting client {e}"
            )
        
    def get_client_by_phone(self, phone: str):
        try:
            client = self.session.query(ClientModel).filter(ClientModel.phone == phone).first()
            return client
        except Exception as e:
            raise HTTPException(
                status_code = status.HTTP_409_CONFLICT,
                detail = f"Error getting client {e}"
            )
        
    def delete_client(self, client_id):
        try:
            client = self.session.query(ClientModel).filter(ClientModel.id == client_id).first()
            self.session.delete(client)
            self.session.commit()
            return True
        except Exception as e:
            raise HTTPException(
                status_code = status.HTTP_409_CONFLICT,
                detail = f"Error deleting client {e}"
            )