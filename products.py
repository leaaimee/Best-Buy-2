class Product:
    """Represents a store product"""


    def __init__(self, name: str, price: float, quantity: int) -> None:
        """Initialize with name, price, and quantity"""
        if not isinstance(name, str):
            raise TypeError("name cannot be empty")
        if not name.strip():
            raise ValueError("name cannot be empty or whitespace only")

        if not isinstance(price, (int, float)):
            raise TypeError("price must be a number")
        if not isinstance(quantity, int):
            raise TypeError("quantity must be an integer")

        if price <= 0:
            raise ValueError("price must be greater than 0")
        if quantity < 0:
            raise ValueError("quantity cannot be negative")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True


    def get_quantity(self) -> int:
        """returns the quantity of the corresponding product"""
        return float(self.quantity)


    def set_quantity(self, quantity: int) -> int:
        """Update product quantity"""
        if not isinstance(quantity, int):
            raise TypeError("quantity must be an integer")
        if self.quantity + quantity < 0:
            raise ValueError(f"Not enough stock. Only {self.quantity} units available")

        self.quantity += quantity

        if self.quantity == 0:
            self.active = False

        return self.quantity


    def is_active(self) -> bool:
        """Returns whether the product is active or not"""
        return self.active


    def deactivate(self):
        """changes the state of the product"""
        self.active = False


    def show(self) -> str:
        """Returns a string representation of the product"""
        return f"Product name: {self.name}, Price: {self.price}$, Stock: {self.quantity} items"


    def buy(self, quantity: int) -> float:
        """checks availability and return the total price"""
        if not isinstance(quantity, int):
            raise TypeError("Quantity must be an integer")
        if quantity > self.quantity:
            raise ValueError(f"Not enough stock. Only {self.quantity} units available")

        self.set_quantity(-quantity)

        return self.price * quantity



# def main():
#     bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
#     print(bose.get_quantity())
#     print(bose.set_quantity(50))
#     print(bose.get_quantity())
#     print(bose.set_quantity(-150))
#     print(bose.get_quantity())
#     print(bose.show())
#     print(bose.buy(100))
#
# if __name__ == "__main__":
#     main()