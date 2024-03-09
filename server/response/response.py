from pydantic import BaseModel
from typing import List, Optional, Dict, Union

class Response(BaseModel):
    """
    Response model for the API

    Attributes:
    - status: int
        The status code of the response
    - message: str
        The message of the response
    - value: Optional[Union[Dict, List]]
        The value of the response, can be a dictionary or a list
    """
    
    status: int
    message: str
    token: str = None
    value: Optional[Union[Dict, List, str]] = None