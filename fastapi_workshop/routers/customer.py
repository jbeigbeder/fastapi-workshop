from fastapi import APIRouter, Depends
from .schemas import customer as schema
from ..database import get_db
from ..repository import customer as repository
from ..models import customer as model

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
    return repository.create(db=db, customer=customer_db)
