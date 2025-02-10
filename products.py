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
        self._price = price
        self._quantity = quantity
        self.active = True
        self.promotion = None


    @property
    def price(self):
        """Getter for price"""
        return self._price

    @price.setter
    def price(self, value: float):
        """Setter for price with validation"""
        if value <= 0:
            raise ValueError("Price must be greater than 0.")
        self._price = value

    @property
    def quantity(self):
        """Getter for quantity"""
        return self._quantity

    @quantity.setter
    def quantity(self, value: int):
        """Setter for quantity with validation"""
        if value < 0:
            raise ValueError("Quantity cannot be negative.")
        self._quantity = value


    def set_promotion(self, promotion):
        """Sets a promotion for the product"""
        self.promotion = promotion


    def is_active(self) -> bool:
        """Returns whether the product is active or not"""
        return self.active


    def deactivate(self):
        """changes the state of the product"""
        self.active = False


    def buy(self, quantity: int) -> float:
        """checks availability and return the total price"""
        if not isinstance(quantity, int):
            raise TypeError("Quantity must be an integer")
        if quantity > self.quantity:
            raise ValueError(f"Not enough stock. Only {self.quantity} units available")

        self.quantity -= quantity

        if self.quantity == 0:
            self.deactivate()

        if self.promotion:
            return self.promotion.apply_promotion(self, quantity)

        return self.price * quantity


    def __str__(self):
        """Returns string representation of the product, including promotion."""
        promo_name = f" (Promotion: {self.promotion.name})" if self.promotion else ""
        return f"{self.name}, Price: ${self.price}, Quantity: {self.quantity}{promo_name}"

    def __gt__(self, other):
        """Compares product prices using > operator"""
        if not isinstance(other, Product):
            return NotImplemented
        return self.price > other.price

    def __lt__(self, other):
        """Compares product prices using < operator"""
        if not isinstance(other, Product):
            return NotImplemented
        return self.price < other.price


class NonStockedProduct(Product):
    """Represents products that don't have a physical stock count"""
    def __init__(self, name: str, price: float):
        super().__init__(name, price, quantity=0)

    def __str__(self):
        """Returns product details, indicating that stock tracking is not required"""
        promo_name = f" (Promotion: {self.promotion.name})" if self.promotion else ""
        return f"{self.name}, Price: ${self.price} (Available){promo_name}"

    def buy(self, amount: int):
        """Processes a purchase without stock limitations"""
        return self.price * amount


class LimitedProduct(Product):
    """Represents a product that has a maximum purchase limit per order"""
    def __init__(self, name: str, price: float, quantity: int, maximum: int):
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def __str__(self):
        """Display product details including purchase limit and promotion"""
        promo_name = f" (Promotion: {self.promotion.name})" if self.promotion else ""
        return f"{self.name}, Price: ${self.price}, Max per order: {self.maximum}{promo_name}"

    def buy(self, amount: int):
        """Restricts purchases to the maximum allowed per order"""
        if amount > self.maximum:
            raise ValueError(f"{self.name} can only be purchased {self.maximum} times per order")
        return super().buy(amount)



def main():
    pass

if __name__ == "__main__":
    main()
