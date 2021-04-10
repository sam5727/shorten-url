from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session
from .. import schemas, database, models

router = APIRouter(
    prefix='/register',
    tags=['Register']
)

@router.post('/', status_code=status.HTTP_200_OK)
def get_shorten_url(request: schemas.Url, response: Response, db: Session = Depends(database.get_db)):
    new_shorten = db.query(models.Url).filter(models.Url.original_url == request.original_url).first()
    if not new_shorten:
        shorten_url = request.original_url[0:4]
        new_shorten = models.Url(original_url=request.original_url, shorten_url=shorten_url)
        db.add(new_shorten)
        db.commit()
        db.refresh(new_shorten)
        response.status_code = status.HTTP_201_CREATED
    return new_shorten