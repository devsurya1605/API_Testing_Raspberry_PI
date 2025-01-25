import requests
import json
from ..config import base_url
from ..API_Classes.EmployeeClass import EmployeeAPI

from ..custom_logger import console_logger, LogLevel, file_logger

c_logger = console_logger(name="Employee_Details", level=LogLevel.INFO)
f_logger = file_logger(name="Employee_Details",level=LogLevel.INFO)


def test_get_employees(api_client):
    c_logger.info(f"Sending GET request to: {base_url}")
    c_logger.info(f"Request headers: {api_client.headers}")
    """
    f_logger.info(f"Sending GET request to: {base_url}")
    f_logger.info(f"Request headers: {api_client.headers}")"""
    try:
        response = api_client.get_employees()
        c_logger.info(f"Response status code: {response.status_code}")
        c_logger.info(f"Response content: {response.text}")
        """
        f_logger.info(f"Response status code: {response.status_code}")
        f_logger.info(f"Response content: {response.text}")"""
        assert response.status_code == 200
        if(response.status_code == 200):
            employeeID = response.json()[-1]["EmployeeId"]
            with open('JSON/lastEmployeeID.json','w') as file:
                json.dump({'EmployeeID': employeeID}, file)
    except requests.exceptions.RequestException as e:
        c_logger.info(f"Request failed with error: {e}")
        assert False

def test_get_employees_negative(api_client_negative):
    c_logger.info(f"Sending GET request to: {base_url}")
    c_logger.info(f"Request headers: {api_client_negative.headers}")
    try:
        response = api_client_negative.get_employees()
        c_logger.info(f"Response status code: {response.status_code}")
        c_logger.info(f"Response content: {response.text}")
        assert response.status_code == 400
    except requests.exceptions.RequestException as e:
        c_logger.info(f"Request failed with error: {e}")
        assert False


def test_create_employee(api_client):
    try:
        response = api_client.create_employee('JSON/newDemoEmployee1.json')
        c_logger.info(f"Response status code: {response.status_code}")
        c_logger.info(f"Response content: {response.text}")
        assert response.status_code == 201
        if(response.status_code == 201):
            employeeID = response.json()["EmployeeId"]
            with open('JSON/lastEmployeeID.json','w') as file:
                json.dump({'EmployeeID': employeeID}, file)
    except requests.exceptions.RequestException as e:
        c_logger.info(f"Request failed with error: {e}")
        assert False


def test_create_employee_negative(api_client):
    try:
        response = api_client.create_employee('JSON/newDemoEmployee1_negative.json')
        c_logger.info(f"Response status code: {response.status_code}")
        c_logger.info(f"Response content: {response.text}")
        assert response.status_code == 201
        if(response.status_code == 201):
            employeeID = response.json()["EmployeeId"]
            with open('JSON/lastEmployeeID.json','w') as file:
                json.dump({'EmployeeID': employeeID}, file)
    except requests.exceptions.RequestException as e:
        c_logger.info(f"Request failed with error: {e}")
        assert False


def test_last_name_Emp(api_client,LastEmployee):
    try:
        response = api_client.get_last_Employee_name(LastEmployee)
        c_logger.info(f"Response status code: {response.status_code}")
        c_logger.info(f"Response content: {response.text}")
        response_dict = response.json()
        print(response_dict)
        assert response.status_code == 200
        assert response_dict['Name'] == 'DemoName1Surya'
    except requests.exceptions.RequestException as e:
        c_logger.info(f"Request failed with error: {e}")
        assert False


def test_last_Emp_Updation(api_client,LastEmployee,):
    try:
        response = api_client.update_employee(LastEmployee,'JSON/updateEmployeeDetails.json')
        c_logger.info(f"Response status code: {response.status_code}")
        c_logger.info(f"Response content: {response.text}")
        response_dict = response.json()
        """
        assert float(response_dict['Experience']) == 1.5"""
        print(response_dict)
        assert response.status_code == 200
    except requests.exceptions.RequestException as e:
        c_logger.info(f"Request failed with error: {e}")
        assert False

def test_last_Emp_Updation_negative(api_client,LastEmployee,):
    try:
        response = api_client.update_employee(LastEmployee,'JSON/updateEmployeeDetails_negative.json')
        c_logger.info(f"Response status code: {response.status_code}")
        c_logger.info(f"Response content: {response.text}")
        response_dict = response.json()
        """
        assert float(response_dict['Experience']) == 1.5"""
        print(response_dict)
        assert response.status_code == 200
    except requests.exceptions.RequestException as e:
        c_logger.info(f"Request failed with error: {e}")
        assert False


def test_add_onboardDate(api_client,LastEmployee):
    try:
        response = api_client.add_onboard_Date(LastEmployee,'JSON/onBoardingDate.json')
        c_logger.info(f"Response status code: {response.status_code}")
        c_logger.info(f"Response content: {response.text}")
        assert response.status_code == 201
    except requests.exceptions.RequestException as e:
        c_logger.info(f"Request failed with error: {e}")
        assert False

def test_add_onboardDate_negative(api_client,LastEmployee):
    try:
        response = api_client.add_onboard_Date(LastEmployee,'JSON/onBoardingDate_negative.json')
        c_logger.info(f"Response status code: {response.status_code}")
        c_logger.info(f"Response content: {response.text}")
        assert response.status_code == 400
    except requests.exceptions.RequestException as e:
        c_logger.info(f"Request failed with error: {e}")
        assert False


def test_add_offboardDate(api_client,LastEmployee):
    try:
        response = api_client.add_offboard_Date(LastEmployee,'JSON/offBoardingDate.json')
        c_logger.info(f"Response status code: {response.status_code}")
        c_logger.info(f"Response content: {response.text}")
        assert response.status_code == 201
    except requests.exceptions.RequestException as e:
        c_logger.info(f"Request failed with error: {e}")
        assert False

def test_add_offboardDate_negative(api_client,LastEmployee):
    try:
        response = api_client.add_offboard_Date(LastEmployee,'JSON/offBoardingDate_negative.json')
        c_logger.info(f"Response status code: {response.status_code}")
        c_logger.info(f"Response content: {response.text}")
        assert response.status_code == 400
    except requests.exceptions.RequestException as e:
        c_logger.info(f"Request failed with error: {e}")
        assert False

def test_delete_last_Emp(api_client,LastEmployee):
    response = api_client.delete_last_Employee(LastEmployee)
    c_logger.info(f"Response status code: {response.status_code}")
    c_logger.info(f"Response content: {response.text}")
    assert response.status_code == 200

