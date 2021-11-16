from pydantic import BaseModel
from datetime import date
from typing import Optional, List


class OrderBase(BaseModel):
    date: date
    total: str


class OrderCreate(OrderBase):
    pass


class Order(OrderBase):
    id: int
    customer_id: int

    class Config:
        orm_mode = True


class CustomerBase(BaseModel):
    name: str
    email: str
    birthday: Optional[date]


class CustomerCreate(CustomerBase):
    pass


class Customer(CustomerBase):
    id: int
    is_active: bool
    orders: List[Order] = []

    class Config:
        orm_mode = True
