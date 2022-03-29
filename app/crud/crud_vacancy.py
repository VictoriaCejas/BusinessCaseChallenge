from aifc import Error
from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.vacancy import Vacancy
from app.schemas.vacancy import VacancyCreate, VacancyInDBBase, VacancyUpdate
from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union
from sqlalchemy import exc



class CRUDVacancy(CRUDBase[Vacancy, VacancyCreate, VacancyUpdate]):
    def create(
        self, db: Session, *, obj_in: VacancyInDBBase
    ) -> Vacancy:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj
       

    def get_db_response(
        self, db: Session, *, skip: int = 0, limit: int = 100
    ) -> List[Vacancy]:
        return (
            db.query(self.model)
            .offset(skip)
            .limit(limit)
            .all()
        )
    
    def get(self, db: Session, vacancy_id: int) -> Optional[Vacancy]:
        return db.query(self.model).filter(self.model.vacancy_id == vacancy_id).first()
    
    def remove(self, db: Session, *, vacancy_id: int) -> Vacancy:
            obj = CRUDVacancy.get(self, db, vacancy_id)
            db.delete(obj)
            db.commit()
            return obj



vacancy = CRUDVacancy(Vacancy)
