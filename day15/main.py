from data import resources, MENU


def is_resource_sufficent(user_menu):
    if resources['water'] < MENU[user_menu]['ingredients']['water']:
        print("water insufficient to make coffee")
    elif resources['milk'] < MENU[user_menu]['ingredients']['milk']:
        print("milk insufficient to make coffee")
    elif resources['milk'] < MENU[user_menu]['ingredients']['coffee']:
        print("coffee powder is not sufficient")
    else:
        return True
    return False


def collect_money(user_menu):
    global money
    print("please insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles? "))
    pennies = int(input("how many pennies?: "))
    total = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    if total < MENU[user_menu]["cost"]:
        print("Sorry that's not enough money. Money refunded")
        return False
    elif total == MENU[user_menu]["cost"]:
        money += MENU[user_menu]["cost"]

        print(f"here is your {user_menu} ☕️. Enjoy!")
        return True
    else:
        money += MENU[user_menu]["cost"]
        print(f"here is your change {round(total - MENU[user_menu]['cost'],2)}")
        print(f"here is your {user_menu} ☕️. Enjoy!")

        return True


money = 0
coffee_machine_on = True
while coffee_machine_on:
    user_menu = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_menu == "report":
        print(f"water: {resources['water']}ml")
        print(f"milk: {resources['milk']}ml")
        print(f"coffee: {resources['coffee']}g")
        print(f"Money: ${money}")
    elif user_menu == "off":
        coffee_machine_on = False
    elif user_menu == "espresso" or "latte" or "cappuccino":
        if is_resource_sufficent(user_menu):
            if collect_money(user_menu):

                resources['water'] -= MENU[user_menu]['ingredients']['water']
                resources['milk'] -= MENU[user_menu]['ingredients']['milk']
                resources['coffee'] -= MENU[user_menu]['ingredients']['coffee']

    else:
        print("invalid option")

