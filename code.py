#write a program by using pizza shop (hint:if enter-1 it shows menu),(if enter -2 its shows order page and calculate the total amount of bill)
#By using function
#Use dictionary


# Pizza menu using dictionary
menu = {
    1: ("Veg Pizza", 200),
    2: ("Cheese Pizza", 250),
    3: ("Paneer Pizza", 300)
}

def show_menu():
    print("---- MENU ----")
    for key in menu:
      print(str(key) + ". " + menu[key][0] + " - " + str(menu[key][1]))


def order_pizza():
    show_menu()
    choice = int(input("Enter pizza number (1-3): "))
    qty = int(input("Enter quantity: "))
    
    if choice in menu:
        name, price = menu[choice]
        total = price * qty 
        print("Your Order:",(qty) * (name))
        print("Total Amount: ", total)
    else:
        print("Invalid pizza choice!")

def pizza_shop():
    print("1. Show Menu")
    print("2. Order Pizza")
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        show_menu()
    elif choice == 2:
        order_pizza()
    else:
        print("invalid menu")

pizza_shop()