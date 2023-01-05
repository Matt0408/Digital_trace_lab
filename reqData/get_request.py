from reqData.response import response
import requests

class get_request:
    def get_data(url):
      
        req = requests.get(url)
        return response(status_code=req.status_code, text=req.text, cookie=req.cookies.get_dict())