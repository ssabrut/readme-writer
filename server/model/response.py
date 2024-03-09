from pydantic import BaseModel
from typing import List, Optional, Dict, Union

class Response(BaseModel):
    """
    Response model for the API
    """
    
    status: int
    message: str
    value: Optional[Union[Dict, List]] = None