from .database import Base
from sqlalchemy import Column, Integer, String

class Url(Base):
    __tablename__ = 'urls'

    id = Column(Integer, primary_key=True, index=True)
    original_url = Column(String)
    shorten_url = Column(String)