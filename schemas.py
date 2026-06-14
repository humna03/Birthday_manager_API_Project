from sqlmodel import Field
from typing import Optional
from datetime import date
from pydantic import BaseModel

class BirthdayCreate(BaseModel): 
    name:str
    birthday:date
    relationship:str
    phone:Optional[str] = None
    notes:Optional[str] = None
class BirthdayResponse(BaseModel):
    id:int
    name:str
    birthday:date
    relationship:str
    phone:Optional[str] = None
    notes:Optional[str] = None
class GiftRequest(BaseModel):
    age:int
    interests:str    
class GiftideaResponse(BaseModel):
    name:str
    relationship:str
    gift_ideas: list[str]
