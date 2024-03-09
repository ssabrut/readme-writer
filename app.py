from fastapi import FastAPI
from server.model import Response

app = FastAPI()

@app.get("/")
def root():
    return Response(status=200, message="success", value={"message": "Hello, World!"})