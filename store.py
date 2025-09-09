from typing import List, Optional

# Import or define the Product class
from products import Product  # Assuming Product class is defined in products.py


class Store:
    """Represents a store containing a list of products.

    Attributes:
        products (list[products.Product]): A list of products available in the store."""
    def __init__(self, products: Optional[List[Product]] = None):
        self.products: List[Product] = products if products is not None else []

    def add_product(self, product):
        """Adds a product to store."""
        self.products.append(product)

    def list_products(self):
        """Lists all products in the store."""
        for product in self.products:
            print(product.show())

    def remove_product(self, product):
        """Removes a product from store."""
        self.products.remove(product)

    def get_total_quantity(self) -> int:
        """Returns the total quantity of all products in the store."""
        return sum(product.get_quantity() for product in self.products)

    def get_all_products(self) -> List[Product]:
        """Returns a list of all products in the store."""
        return self.products

    def order(self, shopping_list) -> float:
        """
        Gets a list of tuples, where each tuple has 2 items:
        Product (Product class) and quantity (int).
        Buys the products and returns the total price of the order.
        """
        total_price = 0.0

        for product, quantity in shopping_list:
            if not isinstance(product, Product):
                raise TypeError("First item in tuple must be a Product")
            if not isinstance(quantity, int):
                raise TypeError("Second item in tuple must be an integer")

            total_price += product.buy(quantity)

        return total_price

######## Testing ########
if __name__ == "__main__":
    product_list = [Product("MacBook Air M2", price=1450, quantity=100),
                    Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    Product("Google Pixel 7", price=500, quantity=250)
                ]

    best_buy = Store(product_list)
    products = best_buy.get_all_products()
    print(best_buy.get_total_quantity())
    print(best_buy.order([(products[0], 1), (products[1], 2)]))

    # from products import Product

    # bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    # mac = Product("MacBook Air M2", price=1450, quantity=100)

    # store = Store()
    # store.add_product(bose)
    # store.add_product(mac)

    # print("Store Products:")
    # store.list_products()

    # print(f"Total Quantity in Store: {store.get_total_quantity()}")

    # shopping_list = [(bose, 2), (mac, 1)]
    # total_order_price = store.order(shopping_list)
    # print(f"Total Order Price: ${total_order_price:.2f}")

    # print("Store Products after order:")
    # store.list_products()
