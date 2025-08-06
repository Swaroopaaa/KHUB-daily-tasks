water = 300
milk = 200
coffee = 100
money = 0

MENU = {
    "frappe": {
        "ingredients": {"water": 50, "milk": 0, "coffee": 18},
        "cost": 120
    },
    "latte": {
        "ingredients": {"water": 200, "milk": 150, "coffee": 24},
        "cost": 130
    },
    "mocha": {
        "ingredients": {"water": 100, "milk": 100, "coffee": 20},
        "cost": 150
    },
    "hot chocolate": {
        "ingredients": {"water": 100, "milk": 150, "coffee": 0},
        "cost": 100
    },
    "cocoa": {
        "ingredients": {"water": 80, "milk": 100, "coffee": 10},
        "cost": 110
    }
}

def is_resource_sufficient(order_ingredients):
    global water, milk, coffee
    if order_ingredients["water"] > water:
        print("Sorry, not enough water.")
        return False
    if order_ingredients["milk"] > milk:
        print("Sorry, not enough milk.")
        return False
    if order_ingredients["coffee"] > coffee:
        print("Sorry, not enough coffee.")
        return False
    return True

def process_coins():
    try:
        total = int(input("Insert money (in ₹): "))
        return total
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return 0

def make_coffee(drink_name, order_ingredients):
    global water, milk, coffee
    water -= order_ingredients["water"]
    milk -= order_ingredients["milk"]
    coffee -= order_ingredients["coffee"]
    print(f"Here is your {drink_name}. Enjoy!")

while True:
    choice = input("What would you like? (frappe/latte/mocha/hot chocolate/cocoa/report/exit): ").lower()

    if choice == "report":
        print(f"Water: {water}ml")
        print(f"Milk: {milk}ml")
        print(f"Coffee: {coffee}g")
        print(f"Money: ₹{money}")
    elif choice == "exit":
        print("Exiting the coffee machine.")
        break
    elif choice in MENU:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            print(f"{choice.capitalize()} costs ₹{drink['cost']}")
            payment = process_coins()
            if payment >= drink["cost"]:
                change = payment - drink["cost"]
                money += drink["cost"]
                if change > 0:
                    print(f"Here is ₹{change} in change.")
                make_coffee(choice, drink["ingredients"])
            else:
                print("Sorry, that's not enough money. Money refunded.")
    else:
        print("Invalid option. Please choose a valid drink.")
