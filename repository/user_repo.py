from sqlalchemy.orm import Session
from models.user import User

def get_user_by_email(db:Session,email:str):
    return db.query(User).filter(User.email == email).first()
    ## select * from users where email == "some@email.com"
    ## first give the first matching row otherwise None

def create_user(db:Session,email:str,password_hash:str):
    user = User(email = email,password_hash = password_hash)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user