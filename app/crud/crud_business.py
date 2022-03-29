from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.business import Business
from app.schemas.business import BusinessCreate, BusinessInDBBase, BusinessUpdate
from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union



class CRUDBusiness(CRUDBase[Business, BusinessCreate, BusinessUpdate]):
    def create(
        self, db: Session, *, obj_in: BusinessInDBBase
    ) -> Business:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_db_response(
        self, db: Session, *, skip: int = 0, limit: int = 100
    ) -> List[Business]:
        return (
            db.query(self.model)
            .offset(skip)
            .limit(limit)
            .all()
        )
    def get(self, db: Session, company_id: int) -> Optional[Business]:
        return db.query(self.model).filter(self.model.company_id == company_id).first()
    
    def remove(self, db: Session, *, company_id: int) -> Business:
            obj = CRUDBusiness.get(self, db, company_id)
            db.delete(obj)
            db.commit()
            return obj

business = CRUDBusiness(Business)
