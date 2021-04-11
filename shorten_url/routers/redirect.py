from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import database
from ..repository import redirect_repo

router = APIRouter(
    tags=['Redirect']
)

@router.get('/{shorten_url}')
def redirect_to_url(shorten_url: str, db: Session = Depends(database.get_db)):
    return redirect_repo.to_shortened_url(shorten_url, db)