from fastapi import APIRouter

router = APIRouter()


@router.get('/hello', tags=['hello'])
def say_hello_world():
    return 'Hello world with FastAPI!'
