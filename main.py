from products import Product
import store

# setup initial stock of inventory
product_list = [ Product("MacBook Air M2", price=1450, quantity=100),
                 Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                 Product("Google Pixel 7", price=500, quantity=250)
               ]
best_buy = store.Store(product_list)

def start():
    """ Simple command-line interface to interact with the store.
    """
    while True:
        print("\nMenu:")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            best_buy.list_products()
        elif choice == '2':
            total_quantity = best_buy.get_total_quantity()
            print(f"Total quantity of all products in store: {total_quantity}")
        elif choice == '3':
            shopping_list = []
            while True:
                product_name = input("Enter product name to buy (or 'done' to finish): ")
                if product_name.lower() == 'done':
                    break
                quantity = int(input(f"Enter quantity of {product_name} to buy: "))

                # Find the product by name
                product = next((p for p in best_buy.get_all_products() if p.name == product_name), None)
                if product:
                    shopping_list.append((product, quantity))
                else:
                    print(f"Product '{product_name}' not found in store.")

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
