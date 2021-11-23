"""repository that interacts with customer model"""
from sqlalchemy import exists
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


def exist_by_email(db: Session, email: str):
    """
    check the existance of a customer using the email
    :param db: database session
    :param email: this email to check
    :return:true if this email is already associated to a customer, false otherwise
    """
    return db.query(exists()).where(model.Customer.email == email)


def get_by_email(db: Session, email: str) -> model.Customer:
    """
    get the Customer by his email
    :param db: database session
    :param email: email of the customer
    :return: a customer, None otherwise
    """
    return db.query(
        model.Customer).filter(model.Customer.email == email).first()
