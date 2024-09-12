import requests
BASE_URL = "http://127.0.0.1:5000/api/v1"
import pytest
import random
import string
token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6dHJ1ZSwiaWF0IjoxNzI2MDU4MjUzLCJqdGkiOiIwNjI1ZWUzMi1jZDA3LTRjZGYtOWMyMi00N2FlODM4OTA4MTMiLCJ0eXBlIjoiYWNjZXNzIiwic3ViIjoiMzQ1Mzk2NDA2MzMwMDY1MDYxNCIsIm5iZiI6MTcyNjA1ODI1MywiY3NyZiI6ImUwYzA2ZjA4LTY4OTgtNDMyMC04ZTFmLTg1N2Y3ZDdiNzlkNCIsImV4cCI6MTcyODY1MDI1MywiYXVkIjoieHBvcy1hdWRpZW5jZSIsInVzZXJ0eXBlIjoiT3duZXIiLCJmaXJzdG5hbWUiOiJzdWphIiwidXNlcm5hbWUiOiI1NDYzNzg4ODk5In0.XPtN5PkmaU3k9SetUVidMJ60Uyxh1w_ZIcVar1D8DsQ"


def generate_random_user():
    '''Generate a random user with the specified fields'''
    def generate_random_string(length):
        '''Generate a random string of given length'''
        return ''.join(random.choices(string.ascii_lowercase, k=length))

    def generate_random_email():
        '''Generate a random email address'''
        return f"{generate_random_string(8)}@gmail.com"

    def generate_random_mobile():
        '''Generate a random 10-digit mobile number'''
        return ''.join(random.choices(string.digits, k=10))

    user_data = {
        "user_name": generate_random_string(8),
        "user_type": "Owner",
        "email": generate_random_email(),
        "mobile": generate_random_mobile(),
        "first_name": generate_random_string(6),
        "last_name": generate_random_string(1).upper(),
        "password": generate_random_string(8),
        "address": "Blore"
    }
    return user_data


class TestCreateBusiness:
    
    def get_data(self):
        return {
        'name': "food business",
        'gstn': "29QHUCR5720V4Z2",
        'telephone':"9967583806",
        'fax': "1-212-555-1234",
        'cin': "L01631KA2010PTC096843",
        'address': "BDA layout",
        'city': "Banglore",
        'pin': "560040",
        'state': "karnataka",
        'country':"India",
        'multi_outlet': True,
        'application_id': 2757640319783666690,
        'dealer_code': "9715398642"
        }
    def get_header(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f"Bearer {token}"
        }

    
    def test_user_register_login(self):
        global token
        url= f"{BASE_URL}/user/register"
        data = generate_random_user()
        response = requests.post(url, json=data)
        assert response.status_code == 201

        data = {
            "user":data['mobile'],
            "password":data['password'],
        }
        url= f"{BASE_URL}/user/dashboard/owner/login"
        response = requests.post(url, json=data)
        print(response.json())
        assert response.status_code == 200
        token = response.json()['access_token']
        print(token)

    @pytest.mark.skip("skipped as every time new user will get crated")
    def test_business_creation_valid_data(self):
        self.test_user_register_login()
        data = self.get_data()
        header = self.get_header()
        url = f"{BASE_URL}/business/register"
        response = requests.post(url, json=data, headers=header)
        assert response.status_code == 201
        assert response.json()['status'] == 'Success'
        assert 'data' in response.json()
        assert 'id' in response.json()['data']

  
    def test_business_creatation_without_token(self):
        '''Testing the creatation of business without token and check the status code and message'''
        data = self.get_data()
        header = self.get_header()
        header.pop('Authorization')

        url = f"{BASE_URL}/business/register"
        response = requests.post(url, json=data,headers=header)
        assert response.status_code == 400
        
        assert response.json()['message'] == 'Invalid Token'
        assert response.json()['status'] == 'Failure'
        print(response.json())
    
    def test_business_creation_without_dealer(self):   
        '''Test create business without dealer code'''     
        data = self.get_data()
        header = self.get_header()
        data.pop('dealer_code')

        url = f"{BASE_URL}/business/register"
        response = requests.post(url, json=data, headers=header)
        assert response.status_code == 400
        assert response.json()['status'] == 'Failure'
        assert 'message' in response.json()
        assert response.json()['message'] == 'Wrong Inputs'

    def test_business_creation_with_incorrect_dealer(self):
        ''' Testing business creation with incorrect dealer code which is not present'''
        data = self.get_data()
        header = self.get_header()
        data['dealer_code'] = "1234562320"   #incorrect dealer code

        url = f"{BASE_URL}/business/register"
        response = requests.post(url, json=data, headers=header)
        assert response.status_code == 404
        assert response.json()['status'] == 'Failure'
        assert 'message' in response.json()
        assert response.json()['message'] == 'Dealer code not found'

    def test_business_creation_with_incorrect_dealer_type(self):
        ''' Testing business creation with incorrect type for dealer where string is required type'''
        data = self.get_data()
        header = self.get_header()
        data['dealer_code'] = 9715398642    # Integer dealer code

        url = f"{BASE_URL}/business/register"
        response = requests.post(url, json=data, headers=header)
        assert response.status_code == 400
        assert response.json()['status'] == 'Failure'
        assert 'message' in response.json()
        assert response.json()['message'] == 'Wrong Inputs'
        
    def test_business_creation_without_name(self):
        '''Testing business creation without passing the name'''
        data = self.get_data()
        header = self.get_header()
        data.pop('name')

        url = f"{BASE_URL}/business/register"
        response = requests.post(url, json=data, headers=header)
        assert response.status_code == 400
        assert response.json()['status'] == 'Failure'
        assert 'message' in response.json()
        assert response.json()['message'] == 'Wrong Inputs'
        
    def test_business_creation_string_type_application_id(self):
        '''Testing the business creation with string type for the application'''
        data = self.get_data()
        header = self.get_header()
        data['application_id'] = "2757640319783666690"

        url = f"{BASE_URL}/business/register"
        response = requests.post(url, json=data, headers=header)
        assert response.status_code == 400
        assert response.json()['status'] == 'Failure'
        assert 'message' in response.json()
        assert response.json()['message'] == 'Wrong Inputs'
          
    def test_business_creation_with_invalid_business_id(self):
        '''Testing business creation with incorrect business id'''
        data = self.get_data()
        header = self.get_header()
        data['application_id'] = 275764031978366669012 #inccorect value

        url = f"{BASE_URL}/business/register"
        response = requests.post(url, json=data, headers=header)
        assert response.status_code == 404
        assert 'message' in response.json()
        assert response.json()['status'] == 'Failure'
        assert 'message' in response.json()
        assert response.json()['message'] == 'No Subscription Plans available for selected application'
       
    #************** Issue ************
    def test_business_creation_with_user_with_business_exist(self):
        '''This is issue with api needs to raise ticket'''
        data = self.get_data()
        header = self.get_header()
        url = f"{BASE_URL}/business/register"
        response = requests.post(url, json=data, headers=header)
        assert response.status_code == 500
        assert response.json()['message'] == 'Internal Server Error'
        
    @pytest.mark.parametrize("gstn", [
        "29QHUCR572",  # GSTN less than 15 characters
        "29QHUCR5720V4Z22777777"  # GSTN greater than 21 characters
    ])
    def test_create_business_with_invalid_gstn(self,gstn):
        '''Test create business with incorrect length gstn'''
        data = self.get_data()
        header = self.get_header()
        data['gstn'] = gstn
        register_url = f"{BASE_URL}/business/register"
        response = requests.post(register_url, json=data, headers=header)
        assert response.status_code == 400
        assert response.json()['status'] == 'Failure'
        assert 'message' in response.json()
        assert response.json()['message'] == 'Wrong Inputs'

    def test_create_business_without_optional_fields(self):
        '''Test create business without optional fields: only required fields provided'''
        self.test_user_register_login()
        data = {
        'name': "cater business",
        'application_id':2757640319783666690,
        'dealer_code': "9715398642"
        }
        header = {
            'Content-Type': 'application/json',
            'Authorization': f"Bearer {token}"
        }
        url = f"{BASE_URL}/business/register"
        response = requests.post(url, json=data, headers=header)
        assert response.status_code == 201
        assert 'status' in response.json()
        assert response.json()['status'] == 'Success'
        assert 'data' in response.json()
        assert 'id' in response.json()['data']

    def test_create_busines_dealer_missing(self):
        '''Test create business with dealer missing'''
        data = self.get_data()
        header = self.get_header()
        data.pop('dealer_code')

        url = f"{BASE_URL}/business/register"
        response = requests.post(url, json=data, headers=header)
        assert response.status_code == 400
        assert 'status' in response.json()
        assert response.json()['status'] == 'Failure'
        assert 'message' in response.json()
        assert response.json()['message'] == 'Wrong Inputs'
       
    @pytest.mark.parametrize("dealer_code", ["1234", "1234567890123456"])
    def test_create_business_with_invalid_length_of_dealer_code(self, dealer_code):
        '''test create business with invalid length of dealer code'''
        data = self.get_data()
        data['dealer_code'] = dealer_code
        header = self.get_header()

        url = f"{BASE_URL}/business/register"
        response = requests.post(url, json=data, headers=header)
        assert response.status_code == 400
        assert response.json()['status'] == 'Failure'
        assert 'message' in response.json()
        assert response.json()['message'] == 'Wrong Inputs'
    
    def test_create_business_with_invalid_dealer_code(self):
        '''test create business with invalid dealer code which is not present'''
        data = self.get_data()
        data['dealer_code'] = "1234567890"
        header = self.get_header()

        url = f"{BASE_URL}/business/register"
        response = requests.post(url, json=data, headers=header)
        assert response.status_code == 404
        assert response.json()['status'] == 'Failure'
        assert 'message' in response.json()
        assert response.json()['message'] == 'Dealer code not found' 
    
 
    def test_create_business_with_extra_payload(self):
        '''test create business with extra payload'''

        data = self.get_data()
        header = self.get_header()
        data['extra'] = "extra"
      
        url = f"{BASE_URL}/business/register"
        response = requests.post(url, json=data, headers=header)
        assert response.status_code == 400
        assert response.json()['status'] == 'Failure'
        assert 'message' in response.json()
        assert response.json()['message'] == 'Wrong Inputs'   

    @pytest.mark.parametrize("multi_outlet", ["string_value", 123, None])
    def test_create_business_with_invalid_multi_outlet(self, multi_outlet):
        '''test create business with invalid multi_outlet values'''
        data = self.get_data()
        data['multi_outlet'] = multi_outlet
        header = self.get_header()

        url = f"{BASE_URL}/business/register"
        response = requests.post(url, json=data, headers=header)
        assert response.status_code == 400
        assert response.json()['status'] == 'Failure'
        assert 'message' in response.json()
        assert response.json()['message'] == 'Wrong Inputs'
    
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
        # ("pin", "A"),  # Pin too short
        # ("pin", "A" * 31),  # Pin too long
        ("state", "A"),  # State too short
        ("state", "A" * 31),  # State too long
        ("country", "A"),  # Country too short
        ("country", "A" * 31) ])  # Country too long
    
    def test_create_business_with_invalid_fields(self, field, value):
        '''test create business with invalid field values'''
        data = self.get_data()
        data[field] = value
        header = self.get_header()

        url = f"{BASE_URL}/business/register"
        response = requests.post(url, json=data, headers=header)
        assert response.status_code == 400
        assert response.json()['status'] == 'Failure'
        assert 'message' in response.json()
        print(response.json())



        
# # # print("accestoken:",token)
#         # header ={
#         #     'Content-Type': 'application/json',
#         #     'Authorization': f"Bearer {token}"
#         # }
#         # url = f"{BASE_URL}/business/login"
#         # response = requests.post(url,json={},headers=header)
#         # print(response.status_code)
#         # # print(response.json())
#         # # assert response.status_code == 200

#         # businessToken = response.json()['access_token']