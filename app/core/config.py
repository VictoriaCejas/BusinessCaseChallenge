from pydantic import AnyHttpUrl, BaseSettings, EmailStr, validator
from typing import List, Optional, Union


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    # BACKEND_CORS_ORIGINS is a JSON-formatted list of origins
    # e.g: '["http://localhost", "http://localhost:4200", "http://localhost:3000", \
    # "http://localhost:8080", "http://local.dockertoolbox.tiangolo.com"]'
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    #LOCAL y TEST
    #SQLALCHEMY_DATABASE_URI: Optional[str] = "postgresql://postgres:admin@localhost/businesscase"
    
    SQLALCHEMY_DATABASE_URI: Optional[str] = "postgresql://biyivvmxdupdpz:d4e9e1605bb22e0dc786c3a4bd4e12ea50e88cac2d989988a05969502b8f8b37@ec2-52-73-155-171.compute-1.amazonaws.com/d7qb0gjp00b3ss"
    
    FIRST_SUPERUSER: EmailStr = "admin@admin.com"

    class Config:
        case_sensitive = True


settings = Settings()
