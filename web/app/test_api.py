import pytest
from app import client

#тест на доступность главной страницы
def test_index():
    response = client.get('/')
    assert response.status_code == 200
#тест на доступность страницы авторизации    
def test_login():
    response = client.get('/auth/login')
    assert response.status_code == 200
#тест на невозможность входа с неправильными данными
def test_invalid_auth():
    data={"login": "v279e",
          "password" : "user256"}
    response = client.post('/auth/login', data=data)
    assert response.status_code == 200
#тест на возможность выхода из аккаунта
def test_logout():
    response=client.get('/auth/logout')
    assert response.status_code==302
