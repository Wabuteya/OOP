# Product class definition
class Product:
    def __init__(self, product_name, price, quantity_in_stock):
        self.product_name = product_name
        self.price = price
        self.quantity_in_stock = quantity_in_stock

    def display_product_info(self):
        #Displays the product's name, price, and available quantity
        print(f"Product: {self.product_name}, Price: ${self.price}, Available: {self.quantity_in_stock} units")

# ShoppingCart class definition
class ShoppingCart:
    total_carts = 0  # Class variable to track the total number of carts created

    def __init__(self):
        self.items = []  # A list to store tuples (product, quantity)
        ShoppingCart.total_carts += 1

    def add_to_cart(self, product, quantity):
        #Adds a product to the cart if the desired quantity is available
        if quantity <= product.quantity_in_stock:
            self.items.append((product, quantity))
            product.quantity_in_stock -= quantity  # Decrease stock
            print(f"Added {quantity} of {product.product_name} to the cart.")
        else:
            print(f"Cannot add {quantity} of {product.product_name}. Only {product.quantity_in_stock} units available.")

    def remove_from_cart(self, product):
        #Removes a product from the cart and restores its stock
        for item in self.items:
            if item[0] == product:
                self.items.remove(item)
                product.quantity_in_stock += item[1]  # Restore stock
                print(f"Removed {item[1]} of {product.product_name} from the cart.")
                return
        print(f"{product.product_name} is not in the cart.")

    def display_cart(self):
        #Displays all the items in the cart
        if not self.items:
            print("The cart is empty.")
        else:
            print("Cart contents:")
            for item in self.items:
                product, quantity = item
                print(f"{product.product_name} - Quantity: {quantity} - Unit Price: ${product.price}")

    def calculate_total(self):
        #Calculates and returns the total price of items in the cart
        total = sum(item[0].price * item[1] for item in self.items)
        return total


# Create at least three Product objects with varying prices and quantities
product1 = Product("FlatScreen", 1200.00, 10)
product2 = Product("Smartwatch", 800.00, 15)
product3 = Product("Phones", 150.00, 25)

# Display product details
print("--- Product List ---")
product1.display_product_info()
product2.display_product_info()
product3.display_product_info()

#Two separate ShoppingCarts
cart1 = ShoppingCart()
cart2 = ShoppingCart()

# Cart 1 operations
print("\n--- Cart 1 Operations ---")
cart1.add_to_cart(product1, 1)  # Add 1 FlatScreen
cart1.add_to_cart(product2, 2)  # Add 2 Smartwatch
cart1.display_cart()  # Display cart items

# Cart 2 operations
print("\n--- Cart 2 Operations ---")
cart2.add_to_cart(product2, 1)  # Add 1 Smartwatch
cart2.add_to_cart(product3, 3)  # Add 3 Phones
cart2.remove_from_cart(product3)  # Remove Phones from the cart
cart2.display_cart()  # Display cart items

# Display the contents of each cart and calculate the total amount
print("\n--- Cart 1 Summary ---")
cart1.display_cart()
print(f"Total for Cart 1: ${cart1.calculate_total()}")

print("\n--- Cart 2 Summary ---")
cart2.display_cart()
print(f"Total for Cart 2: ${cart2.calculate_total()}")

#number of shopping carts created
print(f"\nTotal number of shopping carts created: {ShoppingCart.total_carts}")
