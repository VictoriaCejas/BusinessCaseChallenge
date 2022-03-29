from turtle import title
from typing import List
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.core.config import settings
from app.tests.utils.business import create_random_business


def test_create_business(
    client: TestClient,  db: Session
) -> None:
    data = {"name": "Test", "link": "test.com", "contact_first_name": "TestFirstName", "contact_last_name": "TestLastName", "contact_phone_number": "123", "contact_email": "test@test.com", "country": "Argentina"}
    response = client.post(
        f"{settings.API_V1_STR}/business/", json=data,
    )
    assert response.status_code == 200
    content = response.json()
    assert content["name"] == data["name"]
    assert content["link"] == data["link"]
    assert content["contact_first_name"] == data["contact_first_name"]
    assert content["contact_last_name"] == data["contact_last_name"]
    assert content["contact_phone_number"] == data["contact_phone_number"]
    assert content["contact_email"] == data["contact_email"]
    assert content["country"] == data["country"]
    assert "company_id" in content

def test_get_business(
    client: TestClient, db: Session
) -> None:
    business = create_random_business(db)
    response = client.get(
        f"{settings.API_V1_STR}/business/{business.company_id}",
    )
    assert response.status_code == 200
    content = response.json()
    assert content["name"] == business.name
    assert content["link"] == business.link
    assert content["contact_first_name"] == business.contact_first_name
    assert content["contact_last_name"] == business.contact_last_name
    assert content["contact_phone_number"] == business.contact_phone_number
    assert content["contact_email"] == business.contact_email
    assert content["country"] == business.country

def test_update_business(
    client: TestClient,  db: Session
) -> None:
    business = create_random_business(db)
    data = {"name": "Test", "link": "test.com", "contact_first_name": "TestFirstName", "contact_last_name": "TestLastName", "contact_phone_number": "123", "contact_email": "test@test.com", "country": "Argentina"}
    response = client.put(
        f"{settings.API_V1_STR}/business/{business.company_id}", json=data,
    )
    assert response.status_code == 200
    content = response.json()
    assert content["name"] == data["name"]
    assert content["link"] == data["link"]
    assert content["contact_first_name"] == data["contact_first_name"]
    assert content["contact_last_name"] == data["contact_last_name"]
    assert content["contact_phone_number"] == data["contact_phone_number"]
    assert content["contact_email"] == data["contact_email"]
    assert content["country"] == data["country"]

def test_read_business(
    client: TestClient, db: Session
) -> None:
    business = create_random_business(db)
    response = client.get(
        f"{settings.API_V1_STR}/business/",
    )
    assert response.status_code == 200
    content = [response.json()]
    assert len(content) == 1
  
def test_delete_business(
    client: TestClient,  db: Session
) -> None:
    business = create_random_business(db)
    response = client.delete(
        f"{settings.API_V1_STR}/business/{business.company_id}",
    )
    assert response.status_code == 200
    content = response.json()
   