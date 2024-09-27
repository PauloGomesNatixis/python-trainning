from fastapi import APIRouter
from src.models import Message

#http://127.0.0.1:8000/redoc
#http://localhost:8000/docs
router = APIRouter()

 
#http://localhost:8000/docs/
@router.get("/", response_model=Message)
def read_root():
    return {"message": "Hello, World!"}

#http://localhost:8000/docs/bar/
@router.get("/bar", response_model=Message)
def read_root():
    return {"message": "AAAAA, World!"}


#http://localhost:8000/docs/foo
router_foo = APIRouter(prefix="/foo")
 
#http://localhost:8000/docs/foo
@router_foo.get("/", response_model=Message)
def read_root():
    return {"message": "/foo/ - Hello, World!"}

#http://localhost:8000/docs/foo/bar/
@router_foo.get("/bar", response_model=Message)
def read_root():
    return {"message": "/foo/bar/ - AAAAA, World!"}
