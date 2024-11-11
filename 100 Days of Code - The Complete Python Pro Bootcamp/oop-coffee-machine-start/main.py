from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu_init = Menu()
print(menu_init.get_items())

coffee_machine = CoffeeMaker()
money = MoneyMachine()

flag = True
while flag:
    user_choice = input(f"What would you like?({menu_init.get_items()}): ")

    if user_choice == "report":
        coffee_machine.report()
        money.report()
    elif user_choice == "off":
        flag = False
    else:
        order = menu_init.find_drink(user_choice)
        if order is not None:
            # check machine has enough resources
            if coffee_machine.is_resource_sufficient(order) is False:
                continue
            # take money
            payment = money.make_payment(order.cost)
            if payment:
                coffee_machine.make_coffee(order)


