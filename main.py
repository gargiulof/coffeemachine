MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


MONEY = 0
penny = .01
dime = .10
nickel = .05
quarter = .25
coins = 0
machine_is_on = True


def insert_coins():
    global coins
    global MONEY
    print("Please insert coins")
    quarters = quarter * int(input("How many quarters?:"))
    dimes = dime * int(input("How many dimes?:"))
    nickels = nickel * int(input("How many nickels?:"))
    pennies = penny * int(input("How many pennies?:"))
    coins += sum([quarters, dimes, nickels, pennies])
    MONEY += coins
    return None


def make_espresso():
    global MONEY
    global MENU
    global resources
    global coins
    enough_resources = True
    if resources["water"] < MENU["espresso"]["ingredients"]["water"]:
        print("Sorry there is not enough water.")
        enough_resources = False
    if resources["coffee"] < MENU["espresso"]["ingredients"]["coffee"]:
        print("Sorry there is not enough coffee.")
        enough_resources = False
    if enough_resources:
        insert_coins()
    if MONEY < MENU["espresso"]["cost"]:
        print("Sorry that's not enough money. Money refunded")
        MONEY -= coins
    elif MONEY == MENU["espresso"]["cost"]:
        resources["water"] -= MENU["espresso"]["ingredients"]["water"]
        resources["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]
        print("Here is your espresso. Enjoy!")
    elif MONEY > MENU["espresso"]["cost"]:
        resources["water"] -= MENU["espresso"]["ingredients"]["water"]
        resources["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]
        change = round(coins - MENU["espresso"]["cost"],2)
        MONEY -= change
        print(f"Here is ${change} in change.")
        print("Here is your espresso. Enjoy!")


def make_latte():
    global MONEY
    global MENU
    global resources
    global coins
    enough_resources = True
    if resources["water"] < MENU["latte"]["ingredients"]["water"]:
        print("Sorry there is not enough water.")
        enough_resources = False
    if resources["coffee"] < MENU["latte"]["ingredients"]["coffee"]:
        print("Sorry there is not enough coffee.")
        enough_resources = False
    if resources["milk"] < MENU["latte"]["ingredients"]["milk"]:
        print("Sorry there is not enough milk.")
        enough_resources = False
    if enough_resources:
        insert_coins()
    if MONEY < MENU["latte"]["cost"]:
        print("Sorry that's not enough money. Money refunded")
        MONEY -= coins
    elif MONEY == MENU["latte"]["cost"]:
        resources["water"] -= MENU["latte"]["ingredients"]["water"]
        resources["coffee"] -= MENU["latte"]["ingredients"]["coffee"]
        resources["coffee"] -= MENU["latte"]["ingredients"]["milk"]
        print("Here is your latte. Enjoy!")
    elif MONEY > MENU["latte"]["cost"]:
        resources["water"] -= MENU["latte"]["ingredients"]["water"]
        resources["coffee"] -= MENU["latte"]["ingredients"]["coffee"]
        resources["milk"] -= MENU["latte"]["ingredients"]["milk"]
        change = round(coins - MENU["latte"]["cost"],2)
        MONEY -= change
        print(f"Here is ${change} in change.")
        print("Here is your latte. Enjoy!")


def make_cappuccino():
    global MONEY
    global MENU
    global resources
    global coins
    enough_resources = True
    if resources["water"] < MENU["cappuccino"]["ingredients"]["water"]:
        print("Sorry there is not enough water.")
        enough_resources = False
    if resources["coffee"] < MENU["cappuccino"]["ingredients"]["coffee"]:
        print("Sorry there is not enough coffee.")
        enough_resources = False
    if resources["milk"] < MENU["cappuccino"]["ingredients"]["milk"]:
        print("Sorry there is not enough milk.")
        enough_resources = False
    if enough_resources:
        insert_coins()
    if MONEY < MENU["cappuccino"]["cost"]:
        print("Sorry that's not enough money. Money refunded")
        MONEY -= coins
    elif MONEY == MENU["cappuccino"]["cost"]:
        resources["water"] -= MENU["cappuccino"]["ingredients"]["water"]
        resources["coffee"] -= MENU["cappuccino"]["ingredients"]["coffee"]
        resources["coffee"] -= MENU["cappuccino"]["ingredients"]["milk"]
        print("Here is your cappuccino. Enjoy!")
    elif MONEY > MENU["espresso"]["cost"]:
        resources["water"] -= MENU["cappuccino"]["ingredients"]["water"]
        resources["coffee"] -= MENU["cappuccino"]["ingredients"]["coffee"]
        resources["milk"] -= MENU["cappuccino"]["ingredients"]["milk"]
        change = round(coins - MENU["cappuccino"]["cost"],2)
        MONEY -= change
        print(f"Here is ${change} in change.")
        print("Here is your cappuccino. Enjoy!")




def machine_is_off():
    global machine_is_on
    machine_is_on = False

def machine_on():
    coffee_choice = input("What would you like? Espresso, latte, or cappuccino?").lower()
    report = f"Water: {resources["water"]}ml\nMilk: {resources["milk"]}ml\nCoffee: {resources["coffee"]}g\nMoney: ${MONEY}"
    if coffee_choice == "report":
        print(report)
    elif coffee_choice == "espresso":
        make_espresso()
    elif coffee_choice == "latte":
        make_latte()
    elif coffee_choice == "cappuccino":
        make_latte()
    elif coffee_choice == "off":
        machine_is_off()



while machine_is_on:
    machine_on()