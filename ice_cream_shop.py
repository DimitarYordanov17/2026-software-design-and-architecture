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
