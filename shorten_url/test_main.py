from fastapi import status
from fastapi.testclient import TestClient
from .main import app

client = TestClient(app)

def test_register_invalid_url():
    response = client.post(
        '/register/',
        json={'original_url': 'just_an_invalid_url'}
    )
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

def test_register_url():
    response = client.post(
        '/register/',
        json={'original_url': 'https://www.google.com/'}
    )
    assert response.status_code == status.HTTP_201_CREATED

def test_register_existed_url():
    response = client.post(
        '/register/',
        json={'original_url': 'https://www.google.com/'}
    )
    assert response.status_code == status.HTTP_200_OK

def test_redirect_url_not_found():
    response = client.get(
        '/just_invalid_shortened_url',
        allow_redirects=False
    )
    assert response.status_code == status.HTTP_404_NOT_FOUND

def test_register_and_redirect_to_shortened_url():
    testing_url = 'https://www.leetcode.com/'
    response = client.post(
        '/register/',
        json={'original_url': testing_url}
    )
    assert response.status_code == status.HTTP_201_CREATED
    assert 'shortened_url' in response.json()
    shortened_url = response.json()['shortened_url']
    response = client.get(
        shortened_url,
        allow_redirects=False
    )
    assert response.status_code == status.HTTP_307_TEMPORARY_REDIRECT
    assert response.headers['location'] == testing_url