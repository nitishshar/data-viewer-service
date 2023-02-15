from fastapi import APIRouter
from responses.detail import DetailResponse

router = APIRouter(prefix="/api/v1/demo")


@router.get("/", response_model=DetailResponse)
def hello_world():
    """
    This is a hello world endpoint.

    """
    return DetailResponse(message="Hello World")
