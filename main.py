# TODO: 1. MENU
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
            "milk": 2100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

# TODO: 2. resources
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def check_resource(order_ingredients):
    for item in order_ingredients:
        if resources[item] < order_ingredients[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def subtract_resources(order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here id your {request} ☕️. Enjoy!")

def entry(request, status):
    if request == "report":
        print(f"Water: {resources['water']} ml")
        print(f"Milk: {resources['milk']} ml")
        print(f"Coffee: {resources['coffee']} ml")
        print(f"Income: ${income}")
    elif request == "off":
        status = "off"
        print("Machine is OFF")
        return status
    # elif request == "on":
    #     status == "on"
    #     return status
    else:
        return request


status = "on"
income = 0
# TODO: 3. game
while 1 < 2:
    request = input("What would you like? (espresso/latte/cappuccino): ")
    request = entry(request, status)
    print(request)
    if request != "off" or request != "report":
        order_ingredients = MENU[request]["ingredients"]
        if check_resource(order_ingredients):
            quarters = int(input("how many quarters?: "))
            dimes = int(input("how many dimes?: "))
            nickles = int(input("how many nickles?: "))
            penny = int(input("how many penny?: "))
            total_money = (quarters * 25 + dimes * 10 + nickles * 5 + penny)/100
            total_cost = MENU[request]["cost"]
            income += total_cost
            return_money = total_money - total_cost
            subtract_resources(order_ingredients)
            print(resources)
            print(f"Your return is: ${return_money}.")


