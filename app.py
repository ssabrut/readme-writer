from fastapi import FastAPI
from server.response import Response
import requests

app = FastAPI()

@app.get("/", response_model=Response)
def root():
    return Response(status=200, message="success", value={"message": "Hello, World!"})

@app.post('/api/register', response_model=Response)
def register():
    return Response(status=200, message="success", value=claude.dict())