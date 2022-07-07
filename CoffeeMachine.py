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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


machine_on = True


def process_coins():
    """Returns total from coins inserted"""
    print("Please insert coins.")
    total = 0.25 * int(input("How many quarters?: "))
    total += 0.10 * int(input("How many dimes?: "))
    total += 0.05 * int(input("How many nickles?: "))
    total += 0.01 * int(input("How many pennies?: "))
    return total



def check_resources(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True


while machine_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == 'off':
        machine_on = False
        print("Power off")
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Profit: ${profit}")
    else:
        drink = MENU[choice]
        if check_resources(drink["ingredients"]):
            payment = process_coins()
            if payment < MENU[choice]["cost"]:
                print("Sorry, that's not enough money. Money refunded")
            elif payment >= MENU[choice]["cost"]:
                change = round(payment - MENU[choice]["cost"], 2)
                profit += MENU[choice]["cost"]
                print(f"Here is ${change} in change.")
                print(f"Here is your {choice}. Enjoy!")
