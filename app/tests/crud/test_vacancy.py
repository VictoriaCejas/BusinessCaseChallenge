from re import I
from sqlalchemy.orm import Session
from app import crud
from app.schemas.vacancy import VacancyCreate, VacancyInDBBase, VacancyUpdate
from app.tests.utils.utils import random_email, random_lower_string, random_float, random_int
from datetime import date
from app.tests.utils.business import create_random_business

def test_create_vacancy(db: Session) -> None:
    salary = random_float()
    max_experience= random_int()
    min_experience= random_int()
    vacancy_link= random_lower_string()
    skills = random_lower_string()
    position_name = random_lower_string()

    company = create_random_business(db)
    
    vacancy_in = VacancyInDBBase(company_id=company.company_id, salary=salary, max_experience=max_experience, min_experience=min_experience, vacancy_link=vacancy_link, skills=skills, position_name=position_name, active=True)

    vacancy = crud.vacancy.create(db=db, obj_in=vacancy_in)
    assert vacancy.company_id == company.company_id
    assert vacancy.salary == salary
#
#
def test_get_vacancy(db: Session) -> None:
    salary = random_float()
    max_experience= random_int()
    min_experience= random_int()
    vacancy_link= random_lower_string()
    skills = random_lower_string()
    position_name = random_lower_string()

    company = create_random_business(db)
    vacancy_in = VacancyInDBBase(company_id=company.company_id, salary=salary, max_experience=max_experience, min_experience=min_experience, vacancy_link=vacancy_link, skills=skills, position_name=position_name, active=True)
    vacancy = crud.vacancy.create(db=db, obj_in=vacancy_in)
    stored_vacancy = crud.vacancy.get(db=db, vacancy_id=vacancy.vacancy_id)
    assert stored_vacancy
    assert vacancy.salary == salary


def test_update_vacancy(db: Session) -> None:
    salary = random_float()
    max_experience= random_int()
    min_experience= random_int()
    vacancy_link= random_lower_string()
    skills = random_lower_string()
    position_name = random_lower_string()

    company = create_random_business(db)
    vacancy_in = VacancyInDBBase(company_id=company.company_id, salary=salary, max_experience=max_experience, min_experience=min_experience, vacancy_link=vacancy_link, skills=skills, position_name=position_name, active=True)
    vacancy = crud.vacancy.create(db=db, obj_in=vacancy_in)

    link2 = random_lower_string()
    vacancy_update = VacancyUpdate(vacancy_link=link2)
    vacancy2 = crud.vacancy.update(db=db, db_obj=vacancy, obj_in=vacancy_update)
    assert vacancy.vacancy_link == link2


def test_delete_vacancy(db: Session) -> None:
    salary = random_float()
    max_experience= random_int()
    min_experience= random_int()
    vacancy_link= random_lower_string()
    skills = random_lower_string()
    position_name = random_lower_string()

    company = create_random_business(db)
    vacancy_in = VacancyInDBBase(company_id=company.company_id, salary=salary, max_experience=max_experience, min_experience=min_experience, vacancy_link=vacancy_link, skills=skills, position_name=position_name, active=True)
    vacancy = crud.vacancy.create(db=db, obj_in=vacancy_in)

    vacancy = crud.vacancy.create(db=db, obj_in=vacancy_in)
    vacancy2 = crud.vacancy.remove(db=db, vacancy_id=vacancy.vacancy_id)
    vacancy3 = crud.vacancy.get(db=db, vacancy_id=vacancy.vacancy_id)
    assert vacancy3 is None