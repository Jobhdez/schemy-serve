import requests

url = "http://127.0.0.1:8000/api/"

def create_challenge(url, endpoint, username, password, data):
  re = requests.post(url+endpoint, data=data, auth=(username, password))
  return re.json()
  

def register(url, password, username, first_name, email):
    link = url + 'register/'
    data = {'password': password, 'password2': password, 'username':username, 'first_name': first_name, 'email': email}
    re = requests.post(link, data=data)
    return re.json()
  

def create_app(url, password, username):
  return requests.post(url+'users/apps/', auth=(username, password)).json()

def add_users_to_app(url, app_id, owner_username, owner_password, username):
  data = {'app_id': app_id, 'username':username}
  return requests.post(url+'users/apps/users/user/', data=data, auth=(owner_username, owner_password)).json()

def get_app_users(url, owner_username, owner_password, app_id):
  return requests.get(url+'users/apps/users/'+app_id+'/', auth=(owner_username, owner_password)).json()
  
def challenges(url):
  re = requests.get(url)
  return re.json()

def user_challenges(url, username, password):
  url = url + 'users/challenges/'
  return requests.get(url, auth=(username, password)).json()


def add_problem(url, id, username, password, problem, solution):
  data = {"challenge_id":id, "problem":problem, "solution": solution}
  re = requests.post(url+"users/challenges/problems/", data=data, auth=(username, password))
  return re.json()
