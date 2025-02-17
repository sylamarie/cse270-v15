import requests

# Test 1: Validate successful response with HTTP code 200
def test_valid_user_credentials():
    url = "http://127.0.0.1:8000/users/?username=admin&password=qwerty"
    response = requests.get(url)
    # Check if the response code is 200
    assert response.status_code == 200

# Test 2: Validate unauthorized response with HTTP code 401
def test_invalid_user_credentials():
    url = "http://127.0.0.1:8000/users/?username=admin&password=admin"
    response = requests.get(url)
    # Check if the response code is 401 (Unauthorized)
    assert response.status_code == 401