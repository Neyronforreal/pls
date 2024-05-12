from pydantic import BaseModel
from typing import List


class AddToysValidator(BaseModel):
    toy_type: str
    toy_name: str
    count_toy: int
    toy_price: float


class DeleteToysValidator(BaseModel):
    toy_id: int


class EditToysValidator(BaseModel):
    toy_id: int
    toy_type: str
    toy_name: str
    count_toy: int
    toy_price: float


class Image(BaseModel):
    name: str
    toy_type: str
