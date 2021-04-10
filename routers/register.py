from fastapi import APIRouter

router = APIRouter(
    prefix='/register',
    tags=['Register']
)

@router.post('/{ori_url}')
def get_shorten_url(ori_url: str):
    return ori_url