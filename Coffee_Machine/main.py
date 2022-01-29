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


def check_resources(c_type, w_left, m_left, c_left, money_left):
    if c_type != "report":
        if c_type != "espresso":
            w_left -= MENU[c_type]["ingredients"]["water"]
            m_left -= MENU[c_type]["ingredients"]["milk"]
            c_left -= MENU[c_type]["ingredients"]["coffee"]
            money_left += MENU[c_type]["cost"]
        else:
            w_left -= MENU[c_type]["ingredients"]["water"]
            c_left -= MENU[c_type]["ingredients"]["coffee"]
            money_left += MENU[c_type]["cost"]
        update_list = {"money_in_account": money_left, "water_left": w_left, "milk_left": m_left,
                       "coffee_left": c_left}
        resources_list.update(update_list)
        return resources_list
    else:
        print(f"Water: {w_left}")
        print(f"Milk: {m_left}")
        print(f"Coffee: {c_left}")
        print(f"Money: {money_left}")
        return resources_list


def process_coins(c_type):
    print("Please insert coins.")
    quarters = input("How many quarters?: ")
    dimes = input("How many dimes?: ")
    nickels = input("How many nickels?: ")
    pennies = input("How many pennies?: ")
    total_in_cents = 25 * int(quarters) + 10 * int(dimes) + 5 * int(nickels) + 1 * int(pennies)
    total_in_dollars = total_in_cents / 100
    return total_in_dollars - MENU[c_type]["cost"]


def transaction(change, c_type):
    if int(change) > 0:
        print(f"Here is ${change} in change")
        print(f"Here is your {c_type} Enjoy")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


resources_list = {"money_in_account": 0, "water_left": resources["water"], "milk_left": resources["milk"],
                  "coffee_left": resources["coffee"]}

make_coffee = True
while make_coffee:
    coffee_type = input("What would you like? (espresso/latte/cappuccino): ")
    if coffee_type == "off":
        make_coffee = False
    else:
        if coffee_type == "report":
            check_resources(coffee_type, resources_list["water_left"], resources_list["milk_left"],
                            resources_list["coffee_left"], resources_list["money_in_account"])
        elif coffee_type != "report":
            if resources_list["water_left"] < MENU[coffee_type]["ingredients"]["water"]:
                print("Sorry there is not enough water")
                make_coffee = False
            elif resources_list["coffee_left"] < MENU[coffee_type]["ingredients"]["coffee"]:
                print("Sorry there is not enough coffee")
                make_coffee = False
            elif coffee_type != "espresso":
                if resources_list["milk_left"] < MENU[coffee_type]["ingredients"]["milk"]:
                    print("Sorry there is not enough milk")
                    make_coffee = False
            change_left = process_coins(coffee_type)
            make_coffee = transaction(change_left, coffee_type)
            resources_list = check_resources(coffee_type, resources_list["water_left"], resources_list["milk_left"],
                                             resources_list["coffee_left"], resources_list["money_in_account"])
