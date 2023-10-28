# Smart coffeemachine
class SmartCoffeeMachine:
    def __init__(self):
        self._observers = []

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def prepare_coffee(self, coffee_factory):
        coffee = coffee_factory.create_coffee()
        coffee.prepare()
        message = f"{type(coffee).__name__} is ready"
        self.notify_observers(message)

    def notify_observers(self, message):
        for observer in self._observers:
            observer.update(message)

    # Add method for choosing types of coffee
    def make_coffee(self, coffee_type):
        if coffee_type == "Espresso":
            espresso_factory = EspressoFactory()
            self.prepare_coffee(espresso_factory)
        elif coffee_type == "latte":
            latte_factory = LatteFactory()
            self.prepare_coffee(latte_factory)


