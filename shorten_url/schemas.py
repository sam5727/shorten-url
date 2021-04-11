from pydantic import BaseModel
from typing import Optional

class Url(BaseModel):
    original_url: str
    shorten_url: Optional[str] = None