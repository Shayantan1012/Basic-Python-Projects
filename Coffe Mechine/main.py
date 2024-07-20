from menu import Menu, MenuItem
from coffee_maker import CofeeMachine
from money_mechine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CofeeMachine()
menu = Menu()

is_on = True

while is_on:
    options = menu.get_item()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.get_drinks(choice)
        if coffee_maker.isResourceSuffecient(drink) and money_machine.make_payment(drink.cost):
          coffee_maker.make_Coffee(drink)


