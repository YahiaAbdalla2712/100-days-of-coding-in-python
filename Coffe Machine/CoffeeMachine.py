import CoffeeMachine_data as CM_d

no_enough_milk = False
no_enough_coffee = False
no_enough_water = False

quarters = 0
dimes = 0
nickels = 0
pennies = 0
paid_amt = 0


def calc_amt_paid():
    """
    Calculate the amount of money paid based on the amount entered.
    """
    global quarters, dimes, nickels, pennies
    global paid_amt
    paid_amt = quarters * 0.25 + dimes * 0.1 + nickels * 0.05 + pennies * 0.01


def enter_money():
    """
    Ask the user to enter their money.
    """
    global quarters, dimes, nickels, pennies
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickels = int(input("How many nickels? "))
    pennies = int(input("How many pennies? "))
    calc_amt_paid()


def check_for_change(user_input, paid_amt):
    """check if the user need a change or not"""
    if CM_d.money > (paid_amt - CM_d.MENU[user_input]["cost"]):
        print(f"Here is your change: {paid_amt - CM_d.MENU[user_input]['cost']}")
        CM_d.money -= (paid_amt - CM_d.MENU[user_input]['cost'])
    else:
        print("No enough money in the machine for change")


def check_money(user_input):
    """
    check if the amount of money paid is enough.
    :param user_input: user choice entered by the user.
    """
    global paid_amt
    cost = CM_d.MENU[user_input]['cost']
    if cost > paid_amt:
        print(f"You entered {paid_amt}")
        print("Sorry, that's not enough money. ")
        return False
    CM_d.money += paid_amt
    print(f"Amount of money paid is {paid_amt}")
    return True


def check_resources(user_input):
    """
    Function that checks whether a user input drink can be made or no enough resources for it.
    :param user_input: user choice entered by the user.
    :return: is it possible to make the drink or not.
    """
    global no_enough_water, no_enough_coffee, no_enough_milk
    required_resources = CM_d.MENU[user_input]['ingredients']

    for ingredient, required_amount in required_resources.items():
        available_amount = CM_d.resources.get(ingredient, 0)
        if required_amount > available_amount:
            if ingredient == "water":
                no_enough_water = True
            elif ingredient == "coffee":
                no_enough_coffee = True
            elif ingredient == "milk":
                no_enough_milk = True
            return False

    return True

def modify_resources(user_input):
    """
    Function that modifies the resources (if available) after the user chose a drink to make.
    :param user_input: user choice entered by the user.
    """

    ingredients = CM_d.MENU[user_input]['ingredients']
    for item, amount in ingredients.items():
        CM_d.resources[item] -= amount


def print_not_enough_msg():
    """
    print which resources is missing to fullfil user's drink.
    """
    global no_enough_milk, no_enough_coffee, no_enough_water
    if no_enough_milk:
        print("sorry there is no enough milk for your drink")
        no_enough_milk = False
    elif no_enough_coffee:
        print("sorry there is no enough coffee for your drink")
        no_enough_coffee = False
    elif no_enough_water:
        print("sorry there is no enough water for your drink")
        no_enough_water = False

def coffee_Machine(user_input):
    """
    Turn on the machine.
    :param user_input: user choice entered by the user.
    """
    if user_input == "espresso":
        if check_resources("espresso"):
            enter_money()
            if check_money("espresso"):
                check_for_change("espresso", paid_amt)
                print("Here is your espresso.")
                modify_resources("espresso")
        else:
            print_not_enough_msg()
    elif user_input == "latte":
        if check_resources("latte"):
            enter_money()
            if check_money("latte"):
                check_for_change("latte", paid_amt)
                print("here is your latte.")
                modify_resources("latte")
        else:
            print_not_enough_msg()

    elif user_input == "cappuccino":
        if check_resources("cappuccino"):
            enter_money()
            if check_money("cappuccino"):
                check_for_change("cappuccino", paid_amt)
                print("here is your cappuccino")
                modify_resources("cappuccino")
        else:
            print_not_enough_msg()
while True:
    user_choice = input("What would you like? (espresso/latte/cappuccino):").lower()

    if user_choice == "off":
        break

    elif user_choice == "report":
        print(f"water: {CM_d.resources['water']}ml\nmilk: {CM_d.resources['milk']}ml\ncoffee: {CM_d.resources['coffee']}g\nmoney: {CM_d.money}$\n")

    #for debugging not a real action
    elif user_choice == "refill":
        CM_d.resources["water"] += 300
        CM_d.resources["milk"] += 200
        CM_d.resources["coffee"] += 80

    coffee_Machine(user_choice)