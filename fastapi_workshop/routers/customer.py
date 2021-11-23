"""api to cass customer and order"""
from fastapi import APIRouter, Depends

from .schemas import customer as schema
from ..database import get_db
from ..models import customer as model
from ..repository import customer as custome_repository, order as order_repository

router = APIRouter(prefix="/customers", tags=['customer'])


@router.post(path="/", response_model=schema.Customer)
def create(customer: schema.CustomerCreate, db=Depends(get_db)):
    """
    create a new customer

    a new customer is always active by default

    :param customer:the new customer to create
    :param db: database session (injected)
    :return: the new customer with is id
    """
    customer_db = model.Customer(**customer.dict(), is_active=True)
    return custome_repository.create(db=db, customer=customer_db)


@router.get(path="/", response_model=schema.Customer)
def get(email: str, db=Depends(get_db)):
    """
    get customer by his email

    :param email: email of the customer
    :param db: sata session (injected)
    :return: the customer
    """
    return custome_repository.get_by_email(db, email)


@router.post(path="/{customer_id}/orders", response_model=schema.Order)
def create_order(customer_id: int,
                 order: schema.OrderCreate,
                 db=Depends(get_db)):
    """
    create an new order for the customer

    :param customer_id: id of the customer
    :param order: order to create
    :param db: database session (injected)
    :return: the new order with is id
    """
    order_db = model.Order(date=order.date,
                           total=order.total,
                           customer_id=customer_id)
    return order_repository.create(db, order_db)
