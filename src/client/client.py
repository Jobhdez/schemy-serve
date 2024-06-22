import requests

url = " http://127.0.0.1:8000/api/"

def create_challenge(endpoint, username, password, data):
  re = request.post(url+endpoint, data=data, auth=(username, password))
  return re.json()
  
