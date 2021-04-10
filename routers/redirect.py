from fastapi import APIRouter
from fastapi.responses import RedirectResponse

router = APIRouter(
    tags=['Redirect']
)

@router.get('/{shorten_url}')
def redirect_to_url(shorten_url: str):
    url = 'https://www.google.com/'
    return RedirectResponse(url)