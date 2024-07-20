class CofeeMachine:
    def __init__(self):
        self.resources={
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }
        
    def report(self):
        """Prints a report of all resources."""
        print(f'''water: {self.resources['water']}
                  milk:{self.resources['milk']}
                  coffee:{self.resources['coffee']}
            ''')            
        
    def isResourceSuffecient(self,order):
        canOrder=True
        for ingredient in order.ingredients:
            if(order.ingredients[ingredient]>self.resources[ingredient]):
                canOrder=False
        
        return canOrder
    
    def make_Coffee(self,order):
        for ingredient in order.ingredients:
           self.resources[ingredient]-=order.ingredients[ingredient]
        print(f'Here is your order {order.name}  ☕️ Enjoy!')           
            