from fastapi import FastAPI
from .routers import hello, customer
from .database import engine
from .models import customer as customer_model

# Initialize SQL schema with metadatas of models
customer_model.Base.metadata.create_all(bind=engine)

app = FastAPI()

# add all the APIRouter
app.include_router(hello.router)
app.include_router(customer.router)
