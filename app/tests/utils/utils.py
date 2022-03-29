import random
import string
from typing import Dict

from fastapi.testclient import TestClient

from app.core.config import settings


def random_lower_string() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=32))


def random_email() -> str:
    return f"{random_lower_string()}@{random_lower_string()}.com"

def random_int() -> int:
    return random.randint(1,10000)

def random_float() -> float:
    return random.random()

def get_superuser_token_headers(client: TestClient) -> Dict[str, str]:
    return 
