from sqlalchemy.orm import Session
from business.domain.schemas.business_schemas import BusinessSchema
from business.domain.models.business_model import BusinessModel
from business.domain.repositories.business_repositories import BusinessRepository
from config.database.connection import SessionLocal, get_db
from fastapi import Depends, status, HTTPException


class BusinessRepositoryDb(BusinessRepository):
    def __init__(self, session: Session = Depends(get_db)):
        self.session = session

    def get_business_by_id(self, business_id: int):
        try:
            business = self.session.query(BusinessModel).filter(BusinessModel.id == business_id).first()
            return business
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f"Error getting business {e}"
            )