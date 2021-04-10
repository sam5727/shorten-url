from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.responses import RedirectResponse
from .. import database, models

router = APIRouter(
    tags=['Redirect']
)

@router.get('/{shorten_url}')
def redirect_to_url(shorten_url: str, db: Session = Depends(database.get_db)):
    url = db.query(models.Url).filter(models.Url.shorten_url == shorten_url).first()
    if not url:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'The shorten url, {shorten_url}, not found')
    return RedirectResponse(url.original_url)