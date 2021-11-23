"""
repository that interacts with Order model
"""

from sqlalchemy.orm import Session

from ..models.customer import Order


def create(db: Session, order: Order) -> Order:
    """
    save into db this new order
    :param db: database session
    :param order: model to save
    :return: order refreshed
    """
    db.add(order)
    db.commit()
    db.refresh(order)
    return order
