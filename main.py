#main
if __name__ == "__main__":
    from coffee_factory import EspressoFactory, LatteFactory
    from coffee import Espresso, Latte
    from observer import Observer
    from smart_coffee_machine import SmartCoffeeMachine
    from user import User

    machine = SmartCoffeeMachine()
    user = User("User")

    machine.add_observer(user)

    espresso_factory = EspressoFactory()
    latte_factory = LatteFactory()

    machine.prepare_coffee(espresso_factory)
    machine.prepare_coffee(latte_factory)
