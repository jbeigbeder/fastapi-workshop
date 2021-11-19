from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey
from sqlalchemy.orm import relationship

from ..database import Base


class Order(Base):
    __tablename__ = 'order'
    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date, nullable=False)
    total = Column(String(10), nullable=False)
    customer_id = Column(Integer, ForeignKey("customer.id"))


class Customer(Base):
    __tablename__ = 'customer'
    id = Column(name="id", type_=Integer, primary_key=True, index=True)
    name = Column(name="name", type_=String(50), nullable=False)
    email = Column(name="email",
                   type_=String(100),
                   nullable=False,
                   index=True,
                   unique=True)
    is_active = Column(name='is_active', type_=Boolean, nullable=False)
    birthday = Column(name='birthday', type_=Date)
    orders = relationship(Order)
