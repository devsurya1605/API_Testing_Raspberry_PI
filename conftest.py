import requests
import pytest
import json
from requests.auth import HTTPBasicAuth
from .config import base_url
from .API_Classes.EmployeeClass import EmployeeAPI


@pytest.fixture(scope="session")
def bearer_token():
    auth = HTTPBasicAuth('user1', 'password1')
    response = requests.post(base_url+"/tokens",auth=auth)
    bearer_token = response.json()["access_token"]
    return bearer_token

@pytest.fixture(scope="session",autouse=True)
def api_client(bearer_token):
    headers = {"Authorization": f"Bearer {bearer_token}"}
    return EmployeeAPI(base_url, headers)

@pytest.fixture(scope="session")
def LastEmployee():
    with open('JSON/lastEmployeeID.json','r') as file:
        data = json.load(file)
    return data['EmployeeID']

@pytest.fixture(scope="session")
def bearer_token_negative():
    auth = HTTPBasicAuth('random1', 'random1')
    response = requests.post(base_url+"/tokens",auth=auth)
    bearer_token = response.json()["access_token"]
    return bearer_token

@pytest.fixture(scope="session",autouse=True)
def api_client_negative(bearer_token_negative):
    headers = {"Authorization": f"Bearer {bearer_token_negative}"}
    return EmployeeAPI(base_url, headers)


# @pytest.fixture(scope="session")
# def openFile():
#     with open('JSON/newDemoEmployee1.json','r') as file:
#         data = json.load(file)
#     return data

# @pytest.fixture(scope="session")
# def upadteEmpDetails():
#     with open('JSON/updateEmployeeDetails.json','r') as file:
#         data = json.load(file)
#     return data

# @pytest.fixture(scope="session")
# def onBoardData():
#     with open('JSON/onBoardingDate.json','r') as file:
#         data = json.load(file)
#     return data

# @pytest.fixture(scope="session")
# def offBoardData():
#     with open('JSON/offBoardingDate.json','r') as file:
#         data = json.load(file)
#     return data
