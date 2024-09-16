
import requests
import pytest
BASE_URL = "http://127.0.0.1:5000/api/v1"

@pytest.fixture()
def user_login():
    data = {
        "user": "7777777789",
        "password": "123456"   
    }
    url = f"{BASE_URL}/user/dashboard/owner/login"
    response = requests.post(url, json=data)
    assert response.status_code == 200
    assert 'access_token' in response.json()
    assert 'refresh_token' in response.json()
    return response.json()['access_token']
    
@pytest.fixture
def business_login(user_login):
    url = f"{BASE_URL}/business/login"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {user_login}"
    }
    response = requests.post(url, json={}, headers=headers)
    assert response.status_code == 200
    assert 'access_token' in response.json()
    assert 'refresh_token' in response.json()
    return response.json()['access_token']

@pytest.fixture
def get_header(business_login):
    def _get_header():
        return {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {business_login}"
        }
    return _get_header
def get_data():
    data={
    "name": "Mobile business",
    "gstn": "19QHUCR5720V4Z2",
    "telephone": "8888888888",
    "fax": "1-212-555-1234",
    "cin": "L01631KA2010PTC096843",
    "address": "BDA layout,2nd stage",
    "city": "Banglore",
    "pin": "560040",
    "state": "karnataka ",
    "country": "India",
    "multi_outlet": True
    }
    return data
'''
    "type": 'object',
    'properties': {
        'id': props.uniqueid,
        'name': props.username,
        'gstn': props.GSTN,
        'telephone': props.telephone,
        'fax': props.fax,
        'cin': props.CIN,
        'address': props.address,
        'city': props.city,
        'pin': props.imageUrl,
        'state': props.state,
        'country': props.country,
        'multi_outlet': props.boolean,
        'business_code': props.mobile
    },
    'additionalProperties': False,
    'required': ['name', ]
}
'''

class TestEditBusiness:
   
    def test_business_edit_with_valid(self,get_header):
        '''Test case to login business with valid credentials and data'''
        header= get_header()
        data = get_data()
        print(data)
        data['address'] = "BDA Complex,banglore"
        url = f"{BASE_URL}/business/edit"
        response = requests.put(url, json=data, headers=header)
        print(response.json())
        assert response.status_code == 200
        assert 'status' in response.json()
        assert response.json()['status'] == 'Success'
        assert 'message' in response.json()
        assert response.json()['message'] == 'Business Updated sucessfully'
    
    def test_business_edit_with_header_missing(self):
        '''Test case to edit business without header'''
        url = f"{BASE_URL}/business/edit"
        data = get_data()
        response = requests.put(url, json=data)
        assert response.status_code == 400
        assert 'status' in response.json()
        assert response.json()['status'] == 'Failure'
        assert 'message' in response.json()
        assert response.json()['message'] == 'Invalid Token'
    
    def test_business_edit_with_invalid_header(self,get_header):
        '''Test case to edit business with invalid header'''
        url = f"{BASE_URL}/business/edit"
        header = get_header()
        header['Content-Type'] = "application/xml" #incorrect content type
        data = get_data()
        response = requests.put(url, json=data, headers=header)
        assert response.status_code == 400
        assert 'status' in response.json()
        assert response.json()['status'] == 'Failure'
        assert 'message' in response.json()
        assert response.json()['message'] == 'Wrong Inputs'

    def test_busines_edit_without_required_field(self,get_header):
        '''Test case to edit business without required field - name'''
        url = f"{BASE_URL}/business/edit"
        header = get_header()
        data = get_data()
        del data['name']
        response = requests.put(url, json=data, headers=header)
        assert response.status_code == 400
        assert 'status' in response.json()
        assert response.json()['status'] == 'Failure'
        assert 'message' in response.json()
        assert response.json()['message'] == 'Wrong Inputs'
    
    def test_business_edit_with_extra_fields(self,get_header):
        '''Test case to edit business with extra fields'''
        url = f"{BASE_URL}/business/edit"
        header = get_header()
        data = get_data()
        data['extra'] = 'random field'
       
        response = requests.put(url, json=data, headers=header)
        assert response.status_code == 400
        assert 'status' in response.json()
        assert response.json()['status'] == 'Failure'
        assert 'message' in response.json()
        assert response.json()['message'] == 'Wrong Inputs'
    
    def test_business_edit_with_invalid_method(self,get_header):
        '''Test case to edit business with invalid method'''
        url = f"{BASE_URL}/business/edit"
        header = get_header()
        data = get_data()
        response = requests.post(url, json=data, headers=header)
        assert response.status_code == 405
        assert 'message' in response.json()
        assert response.json()['message'] == 'The method is not allowed for the requested URL.'
        
    @pytest.mark.parametrize("field, value", [
        ("gstn", "short"),  # GSTN too short
        ("gstn", "toolonggstnvalueexceedingmaxlength"),  # GSTN too long
        ("telephone", "123"),  # Telephone too short
        ("telephone", "12345678901234567890"),  # Telephone too long
        ("fax", "1234"),  # Fax too short
        ("fax", "123456789012345678901"),  # Fax too long
        ("cin", "shortcinvalue"),  # CIN too short
        ("cin", "toolongcinvalueexceedingmaxlength"),  # CIN too long
        ("address", "A" * 151),  # Address too long
        ("city", "A"),  # City too short
        ("city", "A" * 31),  # City too long
        ("pin", "A"),  # Pin too short
        ("pin", "A" * 31),  # Pin too long
        ("state", "A"),  # State too short
        ("state", "A" * 31),  # State too long
        ("country", "A"),  # Country too short
        ("country", "A" * 31), # Country too long
        ("multi_outlet", "invalid") ])  # Multi_outlet invalid
    
    def test_business_edit_with_invalid_fields(self, field, value,get_header):
        '''test create business with invalid field values'''
        data = get_data()
        data[field] = value
        header = get_header()

        url = f"{BASE_URL}/business/register"
        response = requests.post(url, json=data, headers=header)
        assert response.status_code == 400
        assert response.json()['status'] == 'Failure'
        assert 'message' in response.json()
        print(response.json())
    


    