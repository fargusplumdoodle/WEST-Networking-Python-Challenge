from typing import List
from pydantic import BaseModel


class User(BaseModel):
    name: str
    role: int
    groups: List[str]


class Brick(BaseModel):
    color: str
    allowed_role: int
    allowed_groups: List[str]
