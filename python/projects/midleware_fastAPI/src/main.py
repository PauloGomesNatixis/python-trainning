from fastapi import FastAPI
from src.routers import router,router_foo
from src.middleware import LogMiddleware

app = FastAPI(
    title="FastAPI Lab", 
    description="A simple API using FastAPI", 
    version="0.1.0"
)


@app.get("/")
def read_root():
    return {"message": "Hello, World!"}


app.add_middleware(LogMiddleware)

app.include_router(router)
app.include_router(router_foo)



#http://127.0.0.1:8000/redoc
#http://127.0.0.1:8000/docs