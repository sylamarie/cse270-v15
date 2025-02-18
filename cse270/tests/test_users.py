import requests
import pytest

# Test 1: Test with valid username and password (expect HTTP 200)
def test_valid_credentials():
    url = "http://127.0.0.1:8000/users/?username=admin&password=qwerty"
    response = requests.get(url)
    
    # Verify that the response is HTTP code 200
    assert response.status_code == 200

# Test 2: Test with valid username but incorrect password (expect HTTP 401)
def test_invalid_credentials():
    url = "http://127.0.0.1:8000/users/?username=admin&password=admin"
    response = requests.get(url)
    
    # Verify that the response is HTTP code 401
    assert response.status_code == 401