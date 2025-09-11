from products import Product
import store

# setup initial stock of inventory
product_list = [ Product("MacBook Air M2", price=1450, quantity=100),
                 Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                 Product("Google Pixel 7", price=500, quantity=250)
               ]
best_buy = store.Store(product_list)


def start():
    """Simple command-line interface that uses numbered product selection."""
    while True:
        print("\nMenu:")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            products = best_buy.get_all_products()  # returns active products by default
            if not products:
                print("No active products in store.")
            else:
                print("\nProducts:")
                for i, p in enumerate(products, start=1):
                    print(f"{i}. {p.name} - Price: ${p.price:.2f} - Quantity: {p.get_quantity()}")

        elif choice == '2':
            total_quantity = best_buy.get_total_quantity()
            print(f"Total quantity of active products in store: {total_quantity}")

        elif choice == '3':
            products = best_buy.get_all_products()
            if not products:
                print("No active products available to order.")
                continue

            shopping_list = []
            while True:
                print("\nAvailable products:")
                for i, p in enumerate(products, start=1):
                    print(f"{i}. {p.name} - ${p.price:.2f} - {p.get_quantity()} available")
                selection = input("Enter product number to buy (or 'done' to finish): ").strip()

                if selection.lower() in ('done', 'd'):
                    break

                # validate product selection
                try:
                    idx = int(selection)
                except ValueError:
                    print("Please enter a valid product number or 'done'.")
                    continue

                if not (1 <= idx <= len(products)):
                    print(f"Please enter a number between 1 and {len(products)}.")
                    continue

                product = products[idx - 1]

                # ask for quantity and validate
                qty_input = input(f"Enter quantity of '{product.name}' to buy (available: {product.get_quantity()}): ").strip()
                try:
                    qty = int(qty_input)
                except ValueError:
                    print("Please enter a valid integer quantity.")
                    continue

                if qty <= 0:
                    print("Quantity must be at least 1.")
                    continue
                if qty > product.get_quantity():
                    print(f"Cannot order {qty}. Only {product.get_quantity()} available.")
                    continue

                shopping_list.append((product, qty))
                print(f"Added {qty} x {product.name} to cart.")

            if not shopping_list:
                print("No items in order.")
                continue

            try:
                total_price = best_buy.order(shopping_list)
                print(f"Total price of your order: ${total_price:.2f}")
            except Exception as e:
                print(f"Error processing order: {e}")

        elif choice == '4':
            print("Thank you for visiting! Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    start()
