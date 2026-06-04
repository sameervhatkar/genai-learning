class ChaiOrder:
    def __init__(self, flavor, size):
        self.flavor = flavor
        self.size = size

    def summary(self):
        return f"{self.size}ml of {self.flavor} chai"
    
order = ChaiOrder("Masala", 200)
print(order.summary())

order_two = ChaiOrder("Ginger", 220)
print(order_two.summary())


