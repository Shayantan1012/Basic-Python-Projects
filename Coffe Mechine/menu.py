class MenuItem:
    "'Model Each Menu Items'"
    def __init__(self, name, water, milk, coffee, cost):
        self.name=name
        self.cost=cost
        self.ingredients={
            "water":water,
            "milk":milk,
            "coffee":coffee,
        }
        
class Menu:
    "'Models the menu wo=ith Drinks'" 
    def __init__(self):
               self.menu=[
            MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5),
            MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.5),
            MenuItem(name="cappuccino", water=250, milk=50, coffee=24, cost=3),
               ]
               
    def get_item(self):
        options=""
        for item in self.menu:
            options+=f"{item.name}/"
        return options
    def get_drinks(self,ordername):
            for item in self.menu:
                if(ordername==item.name):
                    return item   
            print("Your this drink is not present!!!")
        