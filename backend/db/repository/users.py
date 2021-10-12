from sqlalchemy.orm import session

from schemas.users import Usercreate
from db.models.users import User
from core.hashing import Hasher


def create_new_user(user: Usercreate,db:session):
    user=User(username= user.username,email=user.email,hashed_password=Hasher.get_password_hash(user.password),is_active=True,is_superuser=False)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
    