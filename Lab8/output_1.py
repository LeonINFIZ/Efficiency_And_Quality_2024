class Customer:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def get_address(self):
        """
        Повертає адресу користувача.
        """
        return self.address

class Order:
    def __init__(self, customer, product, quantity):
        self.customer = customer
        self.product = product
        self.quantity = quantity

    def print_order_details(self):
        """
        Виводить деталі замовлення.
        """
        print(f"Order for {self.product} x {self.quantity}")
        print(f"Shipping to {self.customer.get_address()}")

    def calculate_shipping_cost(self):
        """
        Обчислює вартість доставки на основі адреси користувача.
        """
        return self.customer.calculate_shipping_cost_for_address()

# Приклад використання класів
customer = Customer("John Doe", "123 Main St, New York, NY 10001")
order = Order(customer, "Laptop", 1)
order.print_order_details()
shipping_cost = order.calculate_shipping_cost()
print(f"Shipping cost: ${shipping_cost:.2f}")