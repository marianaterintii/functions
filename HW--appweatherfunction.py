import requests
from os import system

# HW1: intercative + while/show weather/menu/options
# HW2: move to functions
def showMenu():
    system ("cls")
    print("#" * 50)
    print("1. Todays weather")
    print("0. Exit program")
    print("#" * 50)
    option = int (input (">>> "))
    return option

def dataAutentification():
    city = input ("Enter locality:  ")
    key = "731423682cf01896a7c280cfedeb4f52"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&units=metric"
    res = requests.get(url)
    data = res.json()
    return data

def dataExtraction():
    if data['cod'] == 200:
        temp = data['main']['temp']
        locality = data['name']
        wind_speed = data['wind']['speed']
        weather = data["weather"][0]["description"]
        print (f"Weather in \"{locality}\"")
        print(f"T:{temp}")
        print(f"Wind:{wind_speed}m/s")
        print(f"{weather}")
    elif data['cod'] == '404':
        print(locality, "not found")
    else:
        print ("Not data available")

def confirmation():
        confirmation = input("Would you like to continue(Yes/No):  ")
        if confirmation == "Yes":
             print (input("Hit ENTER to continue")) 
        elif confirmation == "No":
            input ("#" * 50)
        else:
            print("Error")
            input ("#" * 50)



while True:

    option = showMenu()
    if option == 0:
        break
    if option == 1:
        data = dataAutentification()
        dataExtraction()
        confirmation()
        
                   
    
  