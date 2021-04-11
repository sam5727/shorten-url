from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from fastapi.responses import RedirectResponse
from .. import models

def to_shortened_url(shorten_url: str, db: Session):
    url = db.query(models.Url).filter(models.Url.shorten_url == shorten_url).first()
    if not url:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'The shorten url, {shorten_url}, not found')
    return RedirectResponse(url.original_url)