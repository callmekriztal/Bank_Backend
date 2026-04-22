from sqlalchemy.orm import Session
from repository.user_repo import get_user_by_email, create_user
from core.security import hash_password, verify_password, create_access_token


def register_user(db: Session, email: str, password: str):
    existing = get_user_by_email(db, email)
    if existing:
        raise Exception("User already exists")

    hashed = hash_password(password)
    return create_user(db, email, hashed)


def login_user(db: Session, email: str, password: str):
    user = get_user_by_email(db, email)
    if not user:
        raise Exception("Invalid credentials")

    if not verify_password(password, user.password_hash):
        raise Exception("Invalid credentials")

    token = create_access_token({"user_id": user.id})
    return token