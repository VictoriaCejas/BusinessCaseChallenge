from fastapi import APIRouter

from app.api.api_v1.endpoints import vacancies, business

api_router = APIRouter()
api_router.include_router(vacancies.router, prefix="/vacancies", tags=["vacancies"])
api_router.include_router(business.router, prefix="/business", tags=["business"])