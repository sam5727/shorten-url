from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import schemas, database, models

router = APIRouter(
    prefix='/register',
    tags=['Register']
)

@router.post('/')
def get_shorten_url(request: schemas.Url, db: Session = Depends(database.get_db)):
    new_shorten = db.query(models.Url).filter(models.Url.original_url == request.original_url).first()
    if not new_shorten:
        shorten_url = request.original_url[0:4]
        new_shorten = models.Url(original_url=request.original_url, shorten_url=shorten_url)
        db.add(new_shorten)
        db.commit()
        db.refresh(new_shorten)
    return new_shorten