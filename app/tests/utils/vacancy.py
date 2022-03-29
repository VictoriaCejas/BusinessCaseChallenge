from typing import Optional

from sqlalchemy.orm import Session

from app import crud, models
from app.schemas.vacancy import VacancyCreate, VacancyInDBBase
from app.tests.utils.utils import random_email, random_lower_string, random_int, random_float
from app.tests.utils.business import create_random_business

def create_random_vacancy(db: Session) -> models.Vacancy:

    salary = random_float()
    max_experience= random_int()
    min_experience= random_int()
    vacancy_link= random_lower_string()
    skills = random_lower_string()
    position_name = random_lower_string()

    company = create_random_business(db)
    
    vacancy_in = VacancyCreate(company_id=company.company_id, salary=salary, max_experience=max_experience, min_experience=min_experience, vacancy_link=vacancy_link, skills=skills, position_name=position_name)
    vacancy_create = VacancyInDBBase(**vacancy_in.dict(), active=True)

    return crud.vacancy.create(db=db, obj_in=vacancy_create)
