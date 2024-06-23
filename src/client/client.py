import requests

url = " http://127.0.0.1:8000/api/"

def create_challenge(url, endpoint, username, password, data):
  re = requests.post(url+endpoint, data=data, auth=(username, password))
  return re.json()
  

def register(url, password, username, first_name, email):
    link = url + 'register/'
    data = {'password': password, 'password2': password, 'username':username, 'first_name': first_name, 'email': email}
    re = requests.post(link, data=data)
    return re.json()

  
def challenges(url):
  re = requests.get(url)
  return re.json()

def user_challenges(url, username, password):
  url = url + 'users/challenges/'
  return requests.get(url, auth=(username, password)).json()
                      
