'''
- Create a function called signIn()
- This function should take two parameters: username and password
- This function should also contain a local variable: a list of dictionaries 
  which holds the correct username and password for 3 users
- The function should loop through the list of 3 users and in case the username and 
  password parameters does not correspond to any of the users - return None, 
  else - return the dictionary that represents that user'''
from os import system
system ("cls")

def signIn(username, password):
    users = [
        {"username": "Mary", "password": 12345},
        {"username": "John", "password": 56789},
        {"username": "Mike", "password": 54321}
    ]
      
    for user in users:
        if user["username"] == username and user["password"] == password:
            return user
        else:
          return None


# Test
print(signIn("Mary", 12345))
print(signIn("Luca", 56478))