from urllib3 import request

class APIFacts:
    def __init__(self) -> None:
        self.api = "http://localhost:8080/api/v1/"
           
    def by_name(self, name):
        req = request("GET", f"{self.api}?q={name}")
        return self.process_message(req)
        
    def by_id(self, name, id):
        req = request("GET", f"{self.api}?q={name}&i={id}")
        return self.process_message(req)
         
    def all_animes(self) -> dict:
        req = request("GET", f"{self.api}")
        return self.process_message(req)
    
    def process_message(self, req):
        if req.status == 200:
            return req.json()
        else: return {"success": False}
        
def facts(api):
    req = request("GET", api)
    if req.status == 200:
        return req.json()
