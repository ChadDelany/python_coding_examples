# TODO: 2. Check resources sufficient to make drink order.
# TODO: 3. Think clearly with a pad of paper.

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

### sufficient function
def is_resource_sufficient(order_ingredients):
    """Determines if there are enough resources to make the drink."""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]
            print(f'Sorry there is not enough water {item}.')
            return False
    return True


def process_coins():
    """Returns the total calculated from coins inserted."""
    print('Please insert coins.')
    total = int(input('How many quarter?: ')) * 0.25
    total += int(input('How many dimes?: ')) * 0.1
    total += int(input('How many nickles?: ')) * 0.05
    total += int(input('How many pennies?: ')) * 0.01
    return total


is_on = True

while is_on:
    choice = input('What would you like? (espresso/latte/cappuccino): ')
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        print(f'Water: {resources["water"]}ml')
        print(f'Milk: {resources["milk"]}ml')
        print(f'Coffee: {resources["coffee"]}g')
        print(f'Money: {profit}')
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink['ingredients']):
            payment = process_coins()



# TODO: 1. Print report of all coffee machine resources.