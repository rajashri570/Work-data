import requests
import pytest

BASE_URL = "http://127.0.0.1:5000/api/v1"

@pytest.fixture(scope="session")
def user_token():
    data = {
        "user": "9543555536",
        "password": "123456"
    }
    url = f"{BASE_URL}/user/dashboard/owner/login"
    response = requests.post(url, json=data)
    assert response.status_code == 200
    return response.json()['access_token']

@pytest.fixture
def get_header(user_token):
    def _get_header():
        return {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {user_token}"
        }
    return _get_header

class TestLoginBusiness:
    def test_business_login_with_valid(self, get_header):
        '''Test case to login business with valid credentials'''
        url = f"{BASE_URL}/business/login"
        headers = get_header()  # Call the function to get headers
        response = requests.post(url, json={}, headers=headers)
        assert response.status_code == 200, f"Login failed: {response.json()}"
        assert 'access_token' in response.json()
        assert 'refresh_token' in response.json()
    
    def test_BusinessLogin_with_header_missing(self):
        '''Test case to login business without header'''
        url = f"{BASE_URL}/business/login"
        response = requests.post(url, json={})  # header is not passed
        assert response.status_code == 400
        assert 'status' in response.json()
        assert response.json()['status'] == 'Failure'
        assert 'message' in response.json()
        assert response.json()['message'] == 'Invalid Token'

    def test_BusinessLogin_with_invalid_header(self):
        '''Test case to login business with invalid header'''
        url = f"{BASE_URL}/business/login"
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer invalid_token"  # Pass an incorrect token
        }
        response = requests.post(url, json={}, headers=headers)
        assert response.status_code == 400
        assert 'status' in response.json()
        assert response.json()['status'] == 'Failure'
        assert 'message' in response.json()
        assert response.json()['message'] == 'Invalid Token'

    def test_BusinessLogin_with_invalid_method(self,get_header):
        '''Test case to login business with invalid method'''

        url = f"{BASE_URL}/business/login"
        headers = get_header()
        response = requests.put(url, json={}, headers=headers)
        assert response.status_code == 405
        assert 'message' in response.json()
        assert response.json()['message'] == 'The method is not allowed for the requested URL.'

    def test_BusinessLogin_with_extra_field(self,get_header):
        '''Test case to login business with invalid payload'''
        url = f"{BASE_URL}/business/login"
        headers = get_header()
        response = requests.post(url, json={"extra": "extra_value"}, headers=headers)
        assert response.status_code == 200
        assert 'access_token' in response.json()
        assert 'refresh_token' in response.json()