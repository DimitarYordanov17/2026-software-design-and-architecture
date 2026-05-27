class IceCreamShop:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            print("Welcome to the Ice Cream Shop!")
        return cls._instance

    def serve(self, ice_cream):
        print(f"Serving: {ice_cream.describe()} — ${ice_cream.price():.2f}")


class VanillaIceCream:
    def describe(self):
        return "Vanilla"

    def price(self):
        return 2.50


class ChocolateIceCream:
    def describe(self):
        return "Chocolate"

    def price(self):
        return 2.75


class StrawberryIceCream:
    def describe(self):
        return "Strawberry"

    def price(self):
        return 3.00


class IceCreamFactory:
    @staticmethod
    def create(flavor):
        flavors = {
            "vanilla": VanillaIceCream,
            "chocolate": ChocolateIceCream,
            "strawberry": StrawberryIceCream,
        }
        if flavor not in flavors:
            raise ValueError(f"Unknown flavor: {flavor}")
        return flavors[flavor]()


class IceCreamDecorator:
    def __init__(self, ice_cream):
        self._ice_cream = ice_cream

    def describe(self):
        return self._ice_cream.describe()

    def price(self):
        return self._ice_cream.price()


class ChocolateGlazeDecorator(IceCreamDecorator):
    def describe(self):
        return self._ice_cream.describe() + " with Chocolate Glaze"

    def price(self):
        return self._ice_cream.price() + 0.75


class ChocolateSticksDecorator(IceCreamDecorator):
    def describe(self):
        return self._ice_cream.describe() + " with Chocolate Sticks"

    def price(self):
        return self._ice_cream.price() + 0.50


if __name__ == "__main__":
    shop1 = IceCreamShop()
    shop2 = IceCreamShop()
    print(f"Same shop instance: {shop1 is shop2}\n")

    vanilla = IceCreamFactory.create("vanilla")
    chocolate = IceCreamFactory.create("chocolate")
    strawberry = IceCreamFactory.create("strawberry")

    chocolate = ChocolateGlazeDecorator(chocolate)
    strawberry = ChocolateSticksDecorator(ChocolateGlazeDecorator(strawberry))

    shop1.serve(vanilla)
    shop1.serve(chocolate)
    shop1.serve(strawberry)
