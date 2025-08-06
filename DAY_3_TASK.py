water = 300
milk = 200
coffee = 100
money = 0

MENU = {
    "espresso": {
        "ingredients": {"water": 50, "milk": 0, "coffee": 18},
        "cost": 1.5
    },
    "latte": {
        "ingredients": {"water": 200, "milk": 150, "coffee": 24},
        "cost": 2.5
    },
    "cappuccino": {
        "ingredients": {"water": 250, "milk": 100, "coffee": 24},
        "cost": 3.0
    }
}

def is_resource_sufficient(order_ingredients):
    global water, milk, coffee
    if water < order_ingredients["water"]:
        print("Sorry there is not enough water.")
        return False
    if milk < order_ingredients["milk"]:
        print("Sorry there is not enough milk.")
        return False
    if coffee < order_ingredients["coffee"]:
        print("Sorry there is not enough coffee.")
        return False
    return True

def process_coins():
    print("Please insert coins.")
    quarters = int(input("How many quarters?: ")) * 0.25
    dimes = int(input("How many dimes?: ")) * 0.10
    nickels = int(input("How many nickels?: ")) * 0.05
    pennies = int(input("How many pennies?: ")) * 0.01
    return quarters + dimes + nickels + pennies

def is_transaction_successful(money_received, drink_cost):
    global money
    if money_received < drink_cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    change = round(money_received - drink_cost, 2)
    if change > 0:
        print(f"Here is ${change} dollars in change.")
    money += drink_cost
    return True

def make_coffee(drink_name, order_ingredients):
    global water, milk, coffee
    water -= order_ingredients["water"]
    milk -= order_ingredients["milk"]
    coffee -= order_ingredients["coffee"]
    print(f"Here is your {drink_name}. Enjoy! ☕")

while True:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if choice == "off":
        print("Machine turned off.")
        break
    elif choice == "report":
        print(f"Water: {water}ml")
        print(f"Milk: {milk}ml")
        print(f"Coffee: {coffee}g")
        print(f"Money: ${money}")
    elif choice in MENU:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
    else:
        print("Invalid input. Please choose espresso, latte or cappuccino.")
