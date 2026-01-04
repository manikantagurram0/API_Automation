from config.config import Base_url, Dashboard
from SRC.Core.API_Config import APIClient

class dashboard_service(APIClient):
    def dashboard_ser(self, session):
          url=Base_url+Dashboard
          response=self.get(url,session)
          return response