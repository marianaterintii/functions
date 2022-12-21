## app <----- two integers     <------ user
##     <----- choose operation <------ user
##            display result   ------> user
from os import system
system ("cls")

def inputinteger(which):
    print("Enter", which, "integer: ", end= "")
    return int(input())

a = inputinteger("first")
b = inputinteger("second")

operation = input("Choose opeartion (* / + -): ")

result = 0

## HW: add operations if unexisting 
#      operations "wrong operation"

if operation == "+":
    result = a + b
elif operation == "*":
    result = a * b 
elif operation == "/":
    result = a / b  
elif operation == "-":
    result = a - b  
elif operation == "**":
    result = a ** b  
else: 
    print ("wrong operation")

print("Result: ", result)