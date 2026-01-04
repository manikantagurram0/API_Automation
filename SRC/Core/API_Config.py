import requests

class APIClient:
    
    playload={
        "username": "xxxxxxxxxxx@gmail.com", "password": "xxxxxxxxx"
    }
    def __init__(self):
        
        self.header={
            "Content-Type": "application/json",
            "Appid":"103",
            "Systemid":"jobseeker",
            "Accept":"application/json"
        }
        self.session=requests.session()
    def post(self,Url, payload=None,):
        response= self.session.post(Url, json=payload, headers=self.header)
        return self.session,response

    def get(self, Url, session):
        response=session.get(Url, headers=self.header)
        return response


'''  print("respone=",response2.status_code)
    print("totalSearchAppearancesCount",response2.json()["dashBoard"]["totalSearchAppearancesCount"])
    print("last update dated=",response2.json()["dashBoard"]['mod_dt'])'''