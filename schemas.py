from pydantic import BaseModel

class Url(BaseModel):
    original_url: str
    shorten_url: str