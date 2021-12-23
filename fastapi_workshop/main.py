"""start a new FastAPI app, create database objects and register FastAPI routers"""

from fastapi import FastAPI

from .database import engine
from .models import customer as customer_model
from .routers import hello, customer

# Initialize SQL schema with metadatas of models
customer_model.Base.metadata.create_all(bind=engine)

app = FastAPI(title='Workshop: FastApi')

# add all the APIRouter
app.include_router(hello.router)
app.include_router(customer.router)
