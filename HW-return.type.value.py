# creare functii ce returneaza din input valoarea convertita

from os import system
system ("cls")

#value = input("Enter some value: ")

def inputInt( message ):
    print(message, end= "")
    return int(input())

def inputFloat( message ):
    print(message, end= "")
    return float(input())

def inputBoolean( message ):
    print(message, end= "")
    return input()

n = inputInt("Enter the first integer: ")
m = inputInt("Enter the second integer: ")
print( n + m )
print()

n = inputFloat("Enter the first float nr: ")
m = inputFloat("Enter the second float nr: ")
print( n + m )
print()

n = inputBoolean("Enter the first nr: ")
m = inputBoolean("Enter the second nr: ")
print( n > m )


print()


