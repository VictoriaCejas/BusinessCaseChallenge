from typing import Optional

from sqlalchemy.orm import Session

from app import crud, models
from app.schemas.business import BusinessCreate, BusinessInDBBase
from app.tests.utils.utils import random_email, random_lower_string 
from datetime import date

def create_random_business(db: Session) -> models.Business:
   
    name =random_lower_string()
    link = random_lower_string()
    contact_first_name= random_lower_string()
    contact_last_name=random_lower_string()
    contact_phone_number=random_lower_string()
    contact_email=random_email()
    country= random_lower_string()
   
    business_in = BusinessCreate(name=name,link=link,contact_first_name=contact_first_name, contact_last_name=contact_last_name, contact_phone_number=contact_phone_number, contact_email=contact_email, country=country)
    business_create = BusinessInDBBase(**business_in.dict(), date_added=date.today())
    return crud.business.create(db=db, obj_in=business_create)
