water = 300
milk = 200
coffee = 100
money = 0

MENU = {
    "hot chocolate": {
        "ingredients": {"water": 100, "milk": 150, "coffee": 0},
        "cost": 180
    },
    "frappe": {
        "ingredients": {"water": 50, "milk": 100, "coffee": 18},
        "cost": 120
    },
    "mocha": {
        "ingredients": {"water": 200, "milk": 150, "coffee": 24},
        "cost": 220
    },
    "cocoa": {
        "ingredients": {"water": 80, "milk": 120, "coffee": 0},
        "cost": 160
    }
}

def is_resource_sufficient(order_ingredients):
    global water, milk, coffee
    if water < order_ingredients["water"]:
        print("Sorry, there is not enough water.")
        return False
    if milk < order_ingredients["milk"]:
        print("Sorry, there is not enough milk.")
        return False
    if coffee < order_ingredients["coffee"]:
        print("Sorry, there is not enough coffee.")
        return False
    return True

def process_coins():
    print("Please insert  coins.")
    ten = int(input("How many ₹10 coins?: ")) * 10
    five = int(input("How many ₹5 coins?: ")) * 5
    two = int(input("How many ₹2 coins?: ")) * 2
    one = int(input("How many ₹1 coins?: ")) * 1
    total = ten + five + two + one
    return total

def is_transaction_successful(money_received, drink_cost):
    global money
    if money_received < drink_cost:
        print("Sorry, that's not enough money. Money refunded.")
        return False
    change = money_received - drink_cost
    if change > 0:
        print(f"Here is ₹{change} in change.")
    money += drink_cost
    return True

def make_coffee(drink_name, order_ingredients):
    global water, milk, coffee
    water -= order_ingredients["water"]
    milk -= order_ingredients["milk"]
    coffee -= order_ingredients["coffee"]
    print(f"Here is your {drink_name}. ")

while True:
    choice = input("What would you like? (hot chocolate/frappe/mocha/cocoa): ").lower()

    if choice == "off":
        print("Machine turned off.")
        break
    elif choice == "report":
        print(f"Water: {water}ml")
        print(f"Milk: {milk}ml")
        print(f"Coffee: {coffee}g")
        print(f"Money: ₹{money}")
    elif choice in MENU:
        drink = MENU[choice]
        print(f"{choice.title()} costs ₹{drink['cost']}")
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
    else:
        print("Invalid input. Please choose from hot chocolate, frappe, mocha, or cocoa.")
