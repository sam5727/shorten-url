from fastapi import APIRouter, Depends, Response, status, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, database, models
import string, random
from urllib.parse import urlparse

router = APIRouter(
    prefix='/register',
    tags=['Register']
)

@router.post('/', status_code=status.HTTP_200_OK, response_model=schemas.ShownUrl)
def get_shorten_url(request: schemas.Url, response: Response, db: Session = Depends(database.get_db)):
    if not check_is_valid_url(request.original_url):
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=f'{request.original_url} is invalid URL')

    new_shorten = db.query(models.Url).filter(models.Url.original_url == request.original_url).first()
    if not new_shorten:
        shorten_url = get_unique_shorten_url(request.original_url)
        new_shorten = models.Url(original_url=request.original_url, shorten_url=shorten_url)
        db.add(new_shorten)
        db.commit()
        db.refresh(new_shorten)
        response.status_code = status.HTTP_201_CREATED
    return new_shorten

def get_unique_shorten_url(long_url: str):
    alphabet = string.ascii_letters + '0123456789'
    shortened = ''.join(random.choice(alphabet) for _ in range(6))
    return shortened

def check_is_valid_url(long_url: str):
  try:
    result = urlparse(long_url)
    return all([result.scheme, result.netloc])
  except ValueError:
    return False