#coffee_factory
from coffee import Espresso, Latte
# Factory method
class CoffeeFactory:
    def create_coffee(self):
        pass

# Concrete realization of factory
class EspressoFactory(CoffeeFactory):
    def create_coffee(self):
        return Espresso()

class LatteFactory(CoffeeFactory):
    def create_coffee(self):
        return Latte()
