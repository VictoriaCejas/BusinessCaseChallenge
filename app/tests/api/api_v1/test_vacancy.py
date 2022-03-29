from os import system
from turtle import title
from typing import List
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.core.config import settings
from app.tests.utils.vacancy import create_random_vacancy
from app.tests.utils.business import create_random_business


def test_create_vacancies(
    client: TestClient,  db: Session
) -> None:
    company = create_random_business(db)
    data = { "company_id": company.company_id,"salary": 100,"max_experience": 10,"min_experience": 5, "vacancy_link": "link.com", "skills": "SQL", "position_name": "Database Administrator"}
    response = client.post(
        f"{settings.API_V1_STR}/vacancies/", json=data,
    )
    assert response.status_code == 200
    content = response.json()
    assert content["salary"] == data["salary"]
    assert content["max_experience"] == data["max_experience"]
    assert content["min_experience"] == data["min_experience"]
    assert content["skills"] == data["skills"]
    assert content["position_name"] == data["position_name"]
    assert "vacancy_id" in content

def test_get_vacancies(
    client: TestClient, db: Session
) -> None:
    vacancies = create_random_vacancy(db)
    response = client.get(
        f"{settings.API_V1_STR}/vacancies/{vacancies.vacancy_id}",
    )
    assert response.status_code == 200
    content = response.json()
    assert content["salary"] == vacancies.salary
    assert content["max_experience"] == vacancies.max_experience
    assert content["min_experience"] == vacancies.min_experience
    assert content["vacancy_link"] == vacancies.vacancy_link
    assert content["skills"] == vacancies.skills
    assert content["position_name"] == vacancies.position_name

def test_update_vacancies(
    client: TestClient,  db: Session
) -> None:
    vacancies = create_random_vacancy(db)
    data = { "company_id": 1,"salary": 100,"max_experience": 10,"min_experience": 5, "vacancy_link": "link.com", "skills": "SQL", "position_name": "Database Administrator"}
    response = client.put(
        f"{settings.API_V1_STR}/vacancies/{vacancies.vacancy_id}", json=data,
    )
    assert response.status_code == 200
    content = response.json()
    assert content["company_id"] == data["company_id"]
    assert content["salary"] == data["salary"]
    assert content["max_experience"] == data["max_experience"]
    assert content["min_experience"] == data["min_experience"]
    assert content["vacancy_link"] == data["vacancy_link"]
    assert content["skills"] == data["skills"]
    assert content["position_name"] == data["position_name"]

def test_read_vacancies(
    client: TestClient, db: Session
) -> None:
    vacancies = create_random_vacancy(db)
    print(vacancies)
    response = client.get(
        f"{settings.API_V1_STR}/vacancies/",
    )
    assert response.status_code == 200
    content = [response.json()]
    assert len(content) == 1
  
def test_delete_vacancies(
    client: TestClient,  db: Session
) -> None:
    vacancies = create_random_vacancy(db)
    response = client.delete(
        f"{settings.API_V1_STR}/vacancies/{vacancies.vacancy_id}",
    )
    assert response.status_code == 200
    content = response.json()
   