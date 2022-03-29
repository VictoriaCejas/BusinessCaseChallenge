from typing import Optional
from xmlrpc.client import boolean

from pydantic import BaseModel


# Shared properties
class VacancyBase(BaseModel):
    company_id: Optional[int]
    salary: Optional[float]
    max_experience: Optional[int]
    min_experience: Optional[int]
    vacancy_link: Optional[str] = None
    skills: Optional[str]
    position_name : Optional[str]


# Properties to receive on item creation
class VacancyCreate(VacancyBase):
    company_id: int
    salary: float
    max_experience: int
    min_experience: int
    vacancy_link: Optional[str] = None
    skills: str
    position_name: str

# Properties to receive on Vacancy update
class VacancyUpdate(VacancyBase):
    pass


# Properties shared by models stored in DB
class VacancyInDBBase(VacancyBase):
    vacancy_id: Optional[int]
    company_id: int
    salary: float
    max_experience: int
    min_experience: int
    vacancy_link: Optional[str] = None
    skills: str
    position_name: str
    active: bool

    class Config:
            orm_mode = True


# Properties to return to client
class Vacancy(VacancyInDBBase):
    pass


# Properties properties stored in DB
class VacancyInDB(VacancyInDBBase):
    pass
