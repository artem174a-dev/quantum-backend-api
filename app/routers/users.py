from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from ..database.manager import DbManager
from ..schemas.users import User, UserCreate
from ..models.users import User as UserModel
from ..services.auth import get_current_user

router = APIRouter()
db_manager = DbManager()


@router.get("/me")
def read_current_user(email: str = Depends(get_current_user)):
    return {"email": email}


@router.get("/{user_id}", response_model=User)
def read_user(user_id: int, db: Session = Depends(db_manager.get_session), email: str = Depends(get_current_user)):
    db_user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.get("/", response_model=list[User])
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(db_manager.get_session),
               email: str = Depends(get_current_user)):
    users = db.query(UserModel).offset(skip).limit(limit).all()
    return users
