from .BaseClass import BaseAPI
import json

class EmployeeAPI(BaseAPI):
    def __init__(self, base_url, headers):
        super().__init__(base_url, headers)

    def get_employees(self):
        response = self.get("employees")
        return response
    
    def create_employee(self, employee_data:str):
        with open(employee_data,'r') as file:
            data = json.load(file)
        response = self.post("employees/new_employee", json=data)
        return response
    
    def get_last_Employee_name(self,last_Employee_ID):
        response  = self.get("employees/"+last_Employee_ID)
        return response

    def delete_last_Employee(self,last_Employee_ID):
        response  = self.delete("employees/"+last_Employee_ID)
        return response
    
    def update_employee(self,last_Employee_ID,employee_data:str):
        with open(employee_data,'r') as file:
            data = json.load(file)
        response = self.put("employees/"+last_Employee_ID+"/employee_update", json=data)
        return response
    
    def add_onboard_Date(self,last_Employee_ID,employee_onboard_data:str):
        with open(employee_onboard_data,'r') as file:
            data = json.load(file)
        response = self.post("employees/"+last_Employee_ID+"/onboard", json=data)
        return response
    
    def add_offboard_Date(self,last_Employee_ID,employee_offboard_data:str):
        with open(employee_offboard_data,'r') as file:
            data = json.load(file)
        response = self.post("employees/"+last_Employee_ID+"/offboard", json=data)
        return response