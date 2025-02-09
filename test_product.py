from products import Product
import pytest

def test_create_valid_product():

    product = Product("MacBook Air", price=1000, quantity=10)

    assert product.name == "MacBook Air"
    assert product.price == 1000
    assert product.quantity == 10
    assert product.is_active() is True


def test_create_invalid_product_exception():
    # Test for invalid name: empty string
    with pytest.raises(ValueError, match="name cannot be empty"):
        Product("", price=10, quantity=5)

    # Test for invalid name: spaces only
    with pytest.raises(ValueError, match="name cannot be empty or whitespace only"):
        Product("   ", price=10, quantity=5)

    # Test for negative price
    with pytest.raises(ValueError, match="price must be greater than 0"):
        Product("Valid Name", price=-10, quantity=5)

    # Test for invalid quantity: negative value
    with pytest.raises(ValueError, match="quantity cannot be negative"):
        Product("Valid Name", price=10, quantity=-5)


def test_product_becomes_inactive():
    product = Product("MacBook Air", price=1000, quantity=1)
    product.buy(1)

    assert product.is_active() is False


def test_product_purchase():
    product = Product("MacBook Air", price=1000, quantity=5)
    total_price = product.buy(2)

    assert product.quantity == 3
    assert total_price == 2000


def test_check_quantity_exception():
    product = Product("MacBook Air", price=1000, quantity=1)
    error_message = f"Not enough stock. Only {product.quantity} units available"
    with pytest.raises(ValueError, match=error_message):
        product.buy(2)

        product.buy(2)