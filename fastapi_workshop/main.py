from fastapi import FastAPI
from .routers import hello
from .database import engine
from .models import customer

# Initialize SQL schema with metadatas of models
customer.Base.metadata.create_all(bind=engine)

app = FastAPI()

# add all the APIRouter
app.include_router(hello.router)
