import requests

class BaseAPI:
    def __init__(self, base_url, headers):
        self.base_url = base_url
        self.headers = headers

    def get(self, endpoint):
        url = f"{self.base_url}/{endpoint}"
        response = requests.get(url, headers=self.headers)
        return response
    
    def post(self,endpoint,json):
        url = f"{self.base_url}/{endpoint}"
        response = requests.post(url,headers=self.headers,json=json)
        return response
    
    def put(self,endpoint,json):
        url = f"{self.base_url}/{endpoint}"
        response = requests.put(url,headers=self.headers,json=json)
        return response

    def delete(self,endpoint):
        url = f"{self.base_url}/{endpoint}"
        response = requests.delete(url,headers=self.headers)
        return response