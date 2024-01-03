from abc import ABC, abstractmethod
from typing import List
from business.domain.schemas.business_schemas import BusinessSchema

class BusinessRepository(ABC):
    @abstractmethod
    def get_business_by_id(self, business_id: int) -> BusinessSchema:
        pass
