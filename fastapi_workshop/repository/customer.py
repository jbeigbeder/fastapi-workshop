from sqlalchemy.orm import Session

from ..models import customer as model


def create(db: Session, customer: model.Customer) -> model.Customer:
    db.add(customer)
    db.commit()
    db.refresh(customer)
    return customer
