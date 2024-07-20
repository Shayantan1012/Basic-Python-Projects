class MoneyMachine:
    CURRENCY = "$"

    COIN_VALUES = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }
    def __init__(self):
        self.profit=0
        self.money_recieve=0
        
    def report(self):
        '"Print the current proffit"'
        print(f'Money:{self.CURRENCY}{self.profit}')
    def process_coins(self):
        """Returns the total calculated from coins inserted."""
        print("Please insert coins.")
        for coin in self.COIN_VALUES:
           self.money_recieve=int(input(f"How many {coin} you have?:"))*self.COIN_VALUES[coin]
           
        return self.money_recieve     
              
    def make_payment(self, cost):
        """Returns True when payment is accepted, or False if insufficient."""
        self.process_coins()
        if self.money_recieve >= cost:
            change = round(self.money_recieve - cost, 2)
            print(f"Here is {self.CURRENCY}{change} in change.")
            self.profit += cost
            self.money_recieve = 0
            return True
        else:
            print("Sorry that's not enough money. Money refunded.")
            self.money_recieve = 0
            return False
        