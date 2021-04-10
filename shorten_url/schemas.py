from pydantic import BaseModel
from typing import Optional

class Url(BaseModel):
    original_url: str
    shorten_url: Optional[str] = None

class ShownUrl(BaseModel):
    shorten_url: str
    class Config():
        orm_mode = True