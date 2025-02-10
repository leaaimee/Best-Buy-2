from abc import ABC, abstractmethod

class Promotion(ABC):
    """ Abstract base class for promotions """

    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity: int) -> float:
        """ Calculate the discounted price for a given product and quantity """
        pass


class PercentDiscount(Promotion):
    """ Applies a percentage discount to the total price """

    def __init__(self, name: str, percent: float):
        super().__init__(name)
        self.percent = percent

    def apply_promotion(self, product, quantity: int) -> float:
        """ Calculate total price after applying the percentage discount """
        discount = (self.percent / 100) * product.price
        return quantity * (product.price - discount)


class SecondHalfPrice(Promotion):
    """ Applies 'second item at half price' promotion """
    def apply_promotion(self, product, quantity: int) -> float:
        full_price_items = (quantity + 1) // 2
        half_price_items = quantity // 2
        return (full_price_items * product.price) + (half_price_items * product.price * 0.5)


class ThirdOneFree(Promotion):
    """ Applies 'buy 2, get 1 free' promotion """
    def apply_promotion(self, product, quantity: int) -> float:
        sets_of_three = quantity // 3
        remaining_items = quantity % 3
        return (sets_of_three * 2 * product.price) + (remaining_items * product.price)