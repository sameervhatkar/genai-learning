# -----------------------------------------------
# Inheritance Example
# MasalaChai IS-A Chai

class Chai:

    def prepare(self):
        print("Preparing regular chai")


class MasalaChai(Chai):

    def add_spices(self):
        print("Adding ginger, cardamom and cloves")


tea = MasalaChai()

# Method inherited from parent class
tea.prepare()

# Method defined in child class
tea.add_spices()


# -----------------------------------------------
# Composition Example
# ChaiShop HAS-A Chai

class Chai:

    def prepare(self):
        print("Preparing chai")


class ChaiShop:

    def __init__(self):

        # Creating an object of another class
        # ChaiShop HAS-A Chai
        self.chai = Chai()

    def serve(self):

        # Using the Chai object
        self.chai.prepare()

        print("Serving chai")


shop = ChaiShop()

shop.serve()