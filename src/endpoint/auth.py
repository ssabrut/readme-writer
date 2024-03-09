from fastapi import APIRouter, Request
from server.response import Response
from server.engine import database
import time
import hashlib
import jwt

router = APIRouter()
user_collection = database.get_collection('users')
token_collection = database.get_collection('tokens')

@router.post('/register', response_model=Response)
async def register(request: Request):
    """
    Register a new user.

    Args:
        request (Request): The request object.

    Returns:
        Response: The response object.
    """
    
    data = await request.json()

    if 'username' not in data or 'password' not in data:
        return Response(status=409, message="error", value="Username and password are required!")
    
    try:
        if await user_collection.find_one({"username": data['username']}):
            return Response(status=409, message="error", value="Username already exists!")

        data = {
            "username": data['username'],
            "password": hashlib.sha256(data['password'].encode()).hexdigest(),
            "timestamp": time.time()
        }

        user = await user_collection.insert_one(data)
        token = jwt.encode({'_id': str(user.inserted_id)}, "SECRET", algorithm="HS256")
        await token_collection.insert_one({
            "user_id": str(user.inserted_id),
            "token": token,
            "timestamp": time.time()
        })
        
        return Response(status=201, message="success", token=token, value=data)
    except Exception as e:
        return Response(status=500, message="error", value=str(e))