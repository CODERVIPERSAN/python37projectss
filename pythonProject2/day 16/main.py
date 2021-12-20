from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from data import MENU, resources


coffee_maker = CoffeeMaker()

money_machine = MoneyMachine()

menu = Menu()
endgame = False
while not endgame:
    option = menu.get_items()
    menu.name = input(f"enter the coffee {option}")
    if menu.name == "off":
        endgame = True
    elif menu.name == "report":
        report1 = coffee_maker.report()
        money_machine.report()
    else:
        choice = menu.name
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and  money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)



