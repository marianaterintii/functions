'''
- how does the SIGNUP function work in a social network
- Create a function called signUp()
- It should take 3 parameters: username, email, password
- It should verify that the all 3 are strings
- It should verify that the username has at least 5 and at most 12 characters and consists only 
  of latin (a..zA..Z) letters and digits (0..9)
- It should verify the validity of the email address (@, .)
- It should require a password of at least 8 characters long
- It should return a dictionary that contains these three values
- It should raise exceptions when something does not validate
'''
import re # check whether a given string matches a given pattern (using the match function)

def signUP(username, email, password):
  
  if type(username) != str or type(email) != str or type(password) != str:
      raise TypeError("Input values must be strings")
  if not re.match ("[a-zA-Z_][0-9a-zA-Z_]*", username) or len(username) < 5 or len(username) > 12:
      raise ValueError("Invalid username. ")
  if not re.match("(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email):
        raise ValueError("Invalid email address")
  if len(password) < 8:
        raise ValueError(" Invalid password. ")
 
  return {
    "username": username, 
    "email"   : email, 
    "password": password
    }   

username = input ("enter username: ")
email = input ("enter email: ")
password = input ("enter pass: ")

print(signUP(username, email, password))