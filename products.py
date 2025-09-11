class Product:
    """Represents a product with a name, price, and quantity.
    Attributes:
        name (str): The name of the product.
        price (float): The price of the product.
        quantity (int): The available quantity of the product.
        active (bool): Indicates whether the product is active."""

    def __init__(self, name="", price=0.0, quantity=0, active=True):
        if not name.strip():  # empty or whitespace-only string
            raise ValueError("Product name cannot be empty.")
        if price < 0:
            raise ValueError("Price cannot be negative.")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = active

    def get_quantity(self) -> int:
        """Returns the product's quantity."""
        return self.quantity

    def set_quantity(self, quantity):
        """Sets the product's quantity. Quantity cannot be negative.
        If quantity reaches 0, deactivates the product."""
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")

        self.quantity = quantity

        # Auto-deactivate when quantity reaches 0
        if self.quantity == 0:
            self.active = False

    def is_active(self) -> bool:
        """Returns True if the product is active, False otherwise."""
        return self.active

    def set_active(self, active: bool):
        """Sets the product's active status."""
        self.active = active

    def activate(self):
        """Activates the product."""
        self.set_active(True)

    def deactivate(self):
        """Deactivates the product."""
        self.set_active(False)

    def show(self):
        """Returns a string representing the product."""
        return f"{self.name}, Price: ${self.price:.2f}, Quantity: {self.quantity}, Active: {'Yes' if self.active else 'No'}"

    def buy(self, quantity) -> float:
        """
        Buys a given quantity of the product.
        Returns the total price (float) of the purchase.
        Updates the quantity of the product.
        """
        if not self.is_active():
            raise Exception("Product is not active")
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero")
        if quantity > self.quantity:
            raise Exception("Insufficient stock available")

        total_price = self.price * quantity
        self.set_quantity(self.quantity - quantity)
        return total_price


######## Testing ########
if __name__ == "__main__":
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    print(bose.buy(50))
    print(mac.buy(100))
    print(mac.is_active())

    bose.show()
    mac.show()

    bose.set_quantity(1000)
    bose.show()


    # p1 = Product(name="MacBook Air M2", price=1450, quantity=100)
    # print(p1.show())
    # print(f"Buying 2 units of {p1.name} for a total of ${p1.buy(2):.2f}")
    # print(p1.show())

    # p1.deactivate()
    # try:
    #     print(f"Buying 2 units of {p1.name} for a total of ${p1.buy(2):.2f}")
    # except Exception as e:
    #     print(f"Error: {e}")

    # p1.activate()
    # print(f"Buying 2 units of {p1.name} for a total of ${p1.buy(2):.2f}")
    # print(p1.show())

    # try:
    #     p1.set_quantity(-10)
    # except ValueError as ve:
    #     print(f"Error: {ve}")

    # try:
    #     print(f"Buying 200 units of {p1.name} for a total of ${p1.buy(200):.2f}")
    # except Exception as e:
    #     print(f"Error: {e}")
