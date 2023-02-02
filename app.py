
from restaurant import * # * importeaza tot
# contains order data
order = { 
    "items": []
}

order2 = {"name": [], "quantity": [], "total": {"amount": [], "currency": []}}

#################
food = loadFood()
while True:
    option = printMenu()

    if option == 0:
        break
    if option == 1:
        printFood(food)
        input("Hit ENTER to continue")
    if option == 2:
        selected_i = int(input("which item: ")) -1
        print(f"You've selected :<<{food[selected_i] ['name']}>>")
        quantity = int(input("How many: "))
            #HW1: if/else if availabe
        price_per_item = quantity * food[selected_i]['price']['amount']
        if quantity <= int (food[selected_i]['avail']):
            print(
                f"<<{food[selected_i]['name']}>> x {quantity} = {price_per_item: 8.2f}{food[selected_i]['price']['currency']}")
        else: 
            print("Sorry only two available")
        
        #HW2: ask for confirmation (yes/no)
        confirmation = input("Would you like to continue(Yes/No):  ")
        if confirmation == "Yes":
            print (input("Hit ENTER to continue")) 
        if confirmation == "No":
            print ("See you next time")
            input("#" * 50)
        if quantity > (food[selected_i]['avail']) and confirmation == "Yes":
            print ("If you agree to order only two")
            print (input("Hit ENTER to continue")) 
            price_per_item = food[selected_i]['avail'] * food[selected_i]['price']['amount']
            print(
                f"<<{food[selected_i]['name']}>> x {food[selected_i]['avail']} = {price_per_item: 8.2f}{food[selected_i]['price']['currency']}")
            input("#" * 50)

        #HW3: add-> order["items"] (.appened())
        # {
        # "name: "Soup", "Quantity": 10, "total: {"amount": 450, "currency": "MDL"}

        order["items"].append(food[selected_i]['name'])
        order["items"].append( quantity)
        order["items"].append(price_per_item) 
        print("Your order:",order)

        order2["name"].append(food[selected_i]['name'])
        order2["quantity"].append( quantity)
        #order2["total"].append(price_per_item) 
        print("Your order:",order2)

        input("#" * 50)