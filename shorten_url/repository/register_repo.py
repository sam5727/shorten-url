from fastapi import Response, status, HTTPException
from sqlalchemy.orm import Session
from urllib.parse import urlparse
from .. import schemas, models
import string, random

alphabet = string.ascii_letters + '0123456789'

def get_url(request: schemas.Url, response: Response, db: Session):
    ori_url = request.original_url
    if not check_is_valid(ori_url):
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=f'{ori_url} is invalid URL')

    shortened_url = db.query(models.Url).filter(models.Url.original_url == ori_url).first()
    if shortened_url:
        return shortened_url
    while shortened_url is None or db.query(models.Url).filter(models.Url.shorten_url == shortened_url).first() is not None:
        shortened_url = get_shortened_url()
    new_shortened = models.Url(original_url=ori_url, shorten_url=shortened_url)
    db.add(new_shortened)
    db.commit()
    db.refresh(new_shortened)
    response.status_code = status.HTTP_201_CREATED
    return new_shortened

def get_shortened_url():
    shortened = ''.join(random.choice(alphabet) for _ in range(6))
    return shortened

def check_is_valid(long_url: str):
  try:
    result = urlparse(long_url)
    return all([result.scheme, result.netloc])
  except ValueError:
    return False