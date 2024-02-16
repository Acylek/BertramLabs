class CoffeePayer:
    def __init__(self):
        self.coworkers = {}
        self.total_paid = {}

    def add_coworker(self, name, coffee_price):
        self.coworkers[name] = coffee_price
        if name not in self.total_paid:
            self.total_paid[name] = 0

    def get_next_payer(self):
        min_paid = min(self.total_paid.values())
        for name, total in self.total_paid.items():
            if total == min_paid:
                self.total_paid[name] += sum(self.coworkers.values())
                return name

# Initialize the CoffeePayer class
coffee_payer = CoffeePayer()

# Add coworkers and their coffee prices
coffee_payer.add_coworker('Bob', 2.5)
coffee_payer.add_coworker('Jeremy', 2.0)
# Add the rest of the coworkers
# coffee_payer.add_coworker('Name', price)

# Get the next payer
print(coffee_payer.get_next_payer())