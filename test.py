class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, product, quantity):
        self.items.append({"product": product, "quantity": quantity})

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item["product"].price * item["quantity"]
        return total

    def view_cart(self):
        if not self.items:
            print("Your shopping cart is empty.")
        else:
            print("Shopping Cart:")
            for index, item in enumerate(self.items, start=1):
                product = item["product"]
                quantity = item["quantity"]
                print(f"{index}. {product.name} - Price: ${product.price} - Quantity: {quantity}")

def main():
    products = [
        Product("Laptop", 800),
        Product("Smartphone", 500),
        Product("Headphones", 100),
        Product("Tablet", 300),
    ]

    cart = ShoppingCart()

    while True:
        print("\nE-commerce Menu:")
        print("1. Browse Products")
        print("2. Add Product to Cart")
        print("3. View Cart")
        print("4. Checkout")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            print("Available Products:")
            for index, product in enumerate(products, start=1):
                print(f"{index}. {product.name} - Price: ${product.price}")
        elif choice == "2":
            product_index = int(input("Enter the product index to add to the cart: ")) - 1
            if 0 <= product_index < len(products):
                product = products[product_index]
                quantity = int(input("Enter the quantity: "))
                cart.add_item(product, quantity)
                print(f"{quantity} {product.name} added to the cart.")
            else:
                print("Invalid product index.")
        elif choice == "3":
            cart.view_cart()
            print(f"Total: ${cart.calculate_total()}")
        elif choice == "4":
            if cart.items:
                print("Checkout completed. Thank you for your purchase!")
                break
            else:
                print("Your cart is empty. Please add items before checking out.")
        elif choice == "5":
            print("Exiting the E-commerce System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
