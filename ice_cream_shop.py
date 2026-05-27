class IceCreamShop:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            print("Welcome to the Ice Cream Shop!")
        return cls._instance

    def serve(self, ice_cream):
        print(f"Serving: {ice_cream.describe()} — ${ice_cream.price():.2f}")
