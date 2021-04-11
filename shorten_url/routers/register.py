from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session
from .. import schemas, database
from ..repository import register_repo

router = APIRouter(
    prefix='/register',
    tags=['Register']
)

@router.post('/', status_code=status.HTTP_201_CREATED)
def register_shorten_url(request: schemas.Url, response: Response, db: Session = Depends(database.get_db)):
    return register_repo.get_url(request, response, db)