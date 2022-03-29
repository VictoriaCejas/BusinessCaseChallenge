from asyncio.log import logger
from cmath import log
from datetime import date
from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.Business])
def read_business(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    """
    Retrieve businesss.
    """
    business = crud.business.get_multi(db, skip=skip, limit=limit)
    return business


@router.post("/", response_model=schemas.Business)
def create_business(
    *,
    db: Session = Depends(deps.get_db),
    business_in: schemas.BusinessCreate,
) -> Any:
    """
    Create new business.
    """
    business_create = schemas.BusinessInDB(**business_in.dict(), date_added=date.today())
    business = crud.business.create(db=db, obj_in=business_create)
    return business


@router.put("/{company_id}", response_model=schemas.Business)
def update_business(
    *,
    db: Session = Depends(deps.get_db),
    company_id: int,
    business_in: schemas.BusinessUpdate,
) -> Any:
    """
    Update an business.
    """
    business = crud.business.get(db=db, company_id=company_id)
    if not business:
        raise HTTPException(status_code=404, detail="Business not found")

    business = crud.business.update(db=db, db_obj=business, obj_in=business_in)
    return business


@router.get("/{company_id}", response_model=schemas.Business)
def read_business(
    *,
    db: Session = Depends(deps.get_db),
    company_id: int,
) -> Any:
    """
    Get business by ID.
    """
    business = crud.business.get(db=db, company_id=company_id)
    if not business:
        raise HTTPException(status_code=404, detail="Business not found")
    return business


@router.delete("/{company_id}", response_model=schemas.Business)
def delete_business(
    *,
    db: Session = Depends(deps.get_db),
    company_id: int,
) -> Any:
    """
    Delete an business.
    """
    business = crud.business.get(db=db, company_id=company_id)
    if not business:
        raise HTTPException(status_code=404, detail="Business not found")
    business = crud.business.remove(db=db, company_id=company_id)
    return business
