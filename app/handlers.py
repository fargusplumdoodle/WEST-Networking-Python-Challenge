from fastapi import APIRouter, HTTPException
from typing import List, Optional
from .models import User, Brick
from .database import database

router = APIRouter()



@router.get("/bricks", response_model=List[Brick])
def get_bricks():
    return list(database["bricks"].values())

@router.get("/users", response_model=List[User])
def get_users():
    raise HTTPException(status_code=501, detail="Not implemented....... yet!")


@router.get("/users/{name}", response_model=User)
def get_user(name: str):
    raise HTTPException(status_code=501, detail="Not implemented....... yet!")


@router.get("/bricks/{color}")
def can_user_access_brick(color: str, user: Optional[str] = None):
    raise HTTPException(status_code=501, detail="Not implemented....... yet!")


@router.post("/bricks", response_model=Brick)
def create_brick(brick: Brick):
    raise HTTPException(status_code=501, detail="Not implemented....... yet!")


@router.post("/users", response_model=User)
def create_user(user: User):
    raise HTTPException(status_code=501, detail="Not implemented....... yet!")


def can_access(user: User, brick: Brick) -> bool:
    return False
