from sqlalchemy.orm import Session

from ..models import customer as model


def create(db: Session, customer: model.Customer) -> model.Customer:
    """
    Create a new Customer.

    :param db: database session
    :param customer: Customer to write in the database
    :return: the new customer
    """
    db.add(customer)
    db.commit()
    db.refresh(customer)
    return customer
