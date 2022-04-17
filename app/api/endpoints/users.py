from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
# import getDB from app/db/database.py
from app.db.database import getDB

from app.crud.crud_user import user as user_crud
from app.schemas.user import User


router = APIRouter()


@router.get("/", response_model=List[User])
def readUsers(
    db: Session = Depends(getDB),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    """
    Retrieve users.
    """
    users = user_crud.get_multi(db, skip=skip, limit=limit)
    if users:
        raise HTTPException(
            status_code=400,
            detail="The user with this username already exists in the system.",
        )
    return users


@router.post("/", response_model=User)
def createUser(
    *,
    db: Session = Depends(getDB),
    user_in: User,
) -> Any:
    """
    Create new user.
    """
    user = user_crud.get_by_email(db, email=user_in.email)
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this username already exists in the system.",
        )
    user = user_crud.create(db, obj_in=user_in)
    return user


@router.get("/{user_id}", response_model=User)
def readUserByID(
    user_id: int,
    db: Session = Depends(getDB),
) -> Any:
    """
    Get a specific user by id.
    """
    user = user_crud.get(db, id=user_id)
    if not user:
        raise HTTPException(
            status_code=404,
            detail="The user does not exist in the system",
        )
    return user


@router.put("/{user_id}", response_model=User)
def updateUser(
    *,
    db: Session = Depends(getDB),
    user_id: int,
    user_in: User,
) -> Any:
    """
    Update a user.
    """
    user = user_crud.get(db, id=user_id)
    if not user:
        raise HTTPException(
            status_code=404,
            detail="The user does not exist in the system",
        )
    user = user_crud.update(db, db_obj=user, obj_in=user_in)
    return user


@router.delete("/{user_id}", response_model=User)
def deleteUser(
    *,
    db: Session = Depends(getDB),
    user_id: int,
) -> Any:
    """
    Delete an item.
    """
    user = user_crud.get(db, id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Item not found")
    user = user_crud.remove(db=db, id=user_id)
    return user
