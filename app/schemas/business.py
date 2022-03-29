from typing import Optional
from datetime import date

from pydantic import BaseModel, EmailStr, Field


# Shared properties
class BusinessBase(BaseModel):
    name: Optional[str]
    link: Optional[str]
    contact_first_name: Optional[str]
    contact_last_name: Optional[str]
    contact_phone_number: Optional[str]
    contact_email: Optional[EmailStr]
    country: Optional[str]


# Properties to receive on item creation
class BusinessCreate(BusinessBase):
    name: str
    link: str
    contact_first_name: str
    contact_last_name: str
    contact_phone_number: str
    contact_email: EmailStr
    country: str


# Properties to receive on Business update
class BusinessUpdate(BusinessBase):
    pass


# Properties shared by models stored in DB
class BusinessInDBBase(BusinessBase):
    company_id: Optional[int]
    name: str
    link: str
    date_added: date 
    contact_first_name: str
    contact_last_name: str
    contact_phone_number: str
    contact_email: EmailStr
    country: str

    class Config:
        orm_mode = True


# Properties to return to client
class Business(BusinessInDBBase):
    pass


# Properties properties stored in DB
class BusinessInDB(BusinessInDBBase):
    pass
