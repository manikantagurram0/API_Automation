from SRC.Core.API_Config import APIClient
from config.config import Base_url, LoginUrl


class Login_services(APIClient):
    def login(self):
        Url= Base_url+LoginUrl
        payload={
        "username": "xxxxxx@gmail.com", "password": "xxxxxxxxx"
    }
        session, response=self.post(Url, payload)
        return session,response
