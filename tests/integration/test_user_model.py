import pytest
from sqlalchemy import create_engine
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import sessionmaker

from app.database import Base
from app.models.user import User


SQLALCHEMY_DATABASE_URL = "sqlite:///./test_integration.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(scope="function")
def db_session():
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    yield db
    db.close()
    Base.metadata.drop_all(bind=engine)


def test_create_user_success(db_session):
    user = User(
        username="kavya",
        email="kavya@example.com",
        password_hash="hashed_password"
    )
    db_session.add(user)
    db_session.commit()
    db_session.refresh(user)

    assert user.id is not None
    assert user.username == "kavya"
    assert user.email == "kavya@example.com"


def test_username_must_be_unique(db_session):
    user1 = User(
        username="kavya",
        email="kavya1@example.com",
        password_hash="hashed1"
    )
    user2 = User(
        username="kavya",
        email="kavya2@example.com",
        password_hash="hashed2"
    )

    db_session.add(user1)
    db_session.commit()

    db_session.add(user2)
    with pytest.raises(IntegrityError):
        db_session.commit()


def test_email_must_be_unique(db_session):
    user1 = User(
        username="kavya1",
        email="same@example.com",
        password_hash="hashed1"
    )
    user2 = User(
        username="kavya2",
        email="same@example.com",
        password_hash="hashed2"
    )

    db_session.add(user1)
    db_session.commit()

    db_session.add(user2)
    with pytest.raises(IntegrityError):
        db_session.commit()