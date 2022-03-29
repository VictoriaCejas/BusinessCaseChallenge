from typing import TYPE_CHECKING

from app.db.base_class import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Float, Text, Boolean
from sqlalchemy.orm import relationship

if TYPE_CHECKING:
    from .business import Business


class Vacancy(Base):
    vacancy_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    company_id = Column(Integer, ForeignKey("business.company_id"))
    salary = Column(Float)
    max_experience = Column(Integer)
    vacancy_link = Column(String)
    min_experience = Column(Integer)
    skills = Column(Text)
    position_name = Column(String)
    active = Column(Boolean) 
    company = relationship("Business", back_populates="vacancies")