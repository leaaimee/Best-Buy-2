from products import Product

class Store:
    """Represents a store that manages products and handles orders"""
    def __init__(self, products: list[Product]):
        """Initializes the store with a list of products"""
        self.products = products


    def add_product(self, product: Product) -> None:
        """Adds a product to the store"""
        if not isinstance(product, Product):
            raise TypeError("Only Product instances can be added to the store")
        self.products.append(product)


    def remove_product(self, product: Product) -> None:
        """Removes a product from the store"""
        if product not in self.products:
            raise ValueError(f"Product {product.name} not found in store")
        self.products.remove(product)


    def get_total_quantity(self) -> int:
        """Returns the total quantity of all products in the store"""
        return sum(product.get_quantity() for product in self.products)


    def get_all_products(self) -> list:
        """Returns a list of all active products in the store"""
        return [product for product in self.products if product.is_active()]


    def order(self, shopping_list: list[tuple[Product, int]]) -> float:
        """Processes an order & returns the total price"""
        if not all(isinstance(item, tuple) and len(item) == 2 for item in shopping_list):
            raise TypeError("Shopping list must be a list of (Product, int) tuples")
        total_price = 0
        for product, quantity in shopping_list:
            total_price += product.buy(quantity)
        return total_price


def main():

    pass

if __name__ == "__main__":
    main()