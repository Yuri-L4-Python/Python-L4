
name=input("What's your name? ").title()

menu={
    "A": {"item": "Maltesers", "price": 69.50},
    "B": {"item": "Can Coffee", "price": 30.25},
    "C": {"item": "IceTea", "price": 19.00},
    "D": {"item": "Hershey's", "price": 45.50},
    "E": {"item": "IceCream", "price": 32.00},
    "F": {"item": "Oreo", "price": 23.50},}

print(f"\nHello {name}, Welcome to doggo's vending machine.\n")
print(f"What do you want {name}? ")
print("Please type the code for what you want to buy!")
print("Menu:")
for code, item in menu.items():
    print(f"{code}: {item['item']}")

order=input("\nCode: ").upper()

if order not in menu:
    print("I'm sorry, we don't have that here.")
else:
    price=menu[order]["price"]
    print(f"That would be PHP {price}")

    while True:
        pay=float(input("Insert Money: PHP "))

        if pay<price:
            print("That is not enough! Please insert more money.")
        else:
            break

    change=pay-price
    item_name=menu[order]["item"]

    print(f"Your {item_name} has been dispensed.")
    print(f"Here is your change: PHP {change}")
    print("Thank you for coming! Please comeback again soon!")

