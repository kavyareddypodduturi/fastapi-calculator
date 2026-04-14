import pytest
from pydantic import ValidationError
from app.schemas.user import UserCreate


def test_user_create_schema_valid_data():
    user = UserCreate(
        username="kavya",
        email="kavya@example.com",
        password="secret123"
    )

    assert user.username == "kavya"
    assert user.email == "kavya@example.com"
    assert user.password == "secret123"


def test_user_create_schema_invalid_email():
    with pytest.raises(ValidationError):
        UserCreate(
            username="kavya",
            email="not-an-email",
            password="secret123"
        )