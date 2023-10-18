"""Schema for Stock API:"""

from pydantic import BaseModel, Field
class Stockchema(BaseModel):
    name: str = Field(max_length=20) # 
    price: int = Field(gt=0) # Greater than
    code: int = Field(max_length=7)