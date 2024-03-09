from fastapi import FastAPI
from server.response import Response

app = FastAPI()

@app.get("/", response_model=Response)
def root():
    return Response(status=200, message="success", value={"message": "Hello, World!"})