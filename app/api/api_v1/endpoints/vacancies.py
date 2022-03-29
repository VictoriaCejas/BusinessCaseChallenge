from aifc import Error
from asyncio.log import logger
from cmath import log
from datetime import date
import pdb
from re import I
from sqlite3 import IntegrityError
from tkinter import E
from turtle import pd
from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps
from sqlalchemy import exc
from pdb import set_trace


router = APIRouter()


@router.get("/", response_model=List[schemas.Vacancy])
def read_vacancy(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    """
    Retrieve vacancys.
    """
    vacancy = crud.vacancy.get_multi(db, skip=skip, limit=limit)
    return vacancy


@router.post("/", response_model=schemas.Vacancy)
def create_vacancy(
    *,
    db: Session = Depends(deps.get_db),
    vacancy_in: schemas.VacancyCreate,
) -> Any:
    """
    Create new vacancy.
    """
    try:
        vacancy_create = schemas.VacancyInDBBase(**vacancy_in.dict(), active=True)
        vacancy = crud.vacancy.create(db=db, obj_in=vacancy_create)
        return vacancy
    except exc.IntegrityError as e:
         raise HTTPException(status_code = 500, detail= e.orig.diag.message_detail)


@router.put("/{vacancy_id}", response_model=schemas.Vacancy)
def update_vacancy(
    *,
    db: Session = Depends(deps.get_db),
    vacancy_id: int,
    vacancy_in: schemas.VacancyUpdate,
) -> Any:
    """
    Update an vacancy.
    """

    try:
        vacancy = crud.vacancy.get(db=db, vacancy_id=vacancy_id)
        
        if not vacancy:
            raise HTTPException(status_code=404, detail="Vacancy not found")

        vacancy = crud.vacancy.update(db=db, db_obj=vacancy, obj_in=vacancy_in)
        return vacancy
    except exc.IntegrityError as e:
         raise HTTPException(status_code = 500, detail= e.orig.diag.message_detail)



@router.get("/{vacancy_id}", response_model=schemas.Vacancy)
def read_vacancy(
    *,
    db: Session = Depends(deps.get_db),
    vacancy_id: int,
) -> Any:
    """
    Get vacancy by ID.
    """
    vacancy = crud.vacancy.get(db=db, vacancy_id=vacancy_id)
    if not vacancy:
        raise HTTPException(status_code=404, detail="Vacancy not found")
    return vacancy


@router.delete("/{vacancy_id}", response_model=schemas.Vacancy)
def delete_vacancy(
    *,
    db: Session = Depends(deps.get_db),
    vacancy_id: int,
) -> Any:
    """
    Delete an vacancy.
    """
    vacancy = crud.vacancy.get(db=db, vacancy_id=vacancy_id)
    if not vacancy:
        raise HTTPException(status_code=404, detail="Vacancy not found")
    vacancy = crud.vacancy.remove(db=db, vacancy_id=vacancy_id)
    return vacancy
