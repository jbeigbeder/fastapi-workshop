from fastapi import APIRouter

router = APIRouter()


@router.get('/hello', tags=['hello'])
def say_hello_world():
    return 'Hello world with FastAPI!'


@router.get("/hello/{name}")
async def say_hello(name: str, echo: int = 1):
    """Say hello to someone

    Parameters
    ----------
    name: name (required)
    echo: nombre of time the API say hello (optional, default to 1)
    """
    message = "Hello " + name + "! "
    return {"message": message * echo}
