class Product:
    def __init__(self, product_id, name, category, price):
        self._product_id = product_id 
        self._name = name  
        self._category = category  
        self._price = price  

    def get_product_id(self):
        """
        Повертає ідентифікатор продукту.
        """
        return self._product_id

    def get_name(self):
        """
        Повертає назву продукту.
        """
        return self._name

    def get_category(self):
        """
        Повертає категорію продукту.
        """
        return self._category

    def get_price(self):
        """
        Повертає ціну продукту.
        """
        return self._price


class InventoryManagement:
    def __init__(self, products):
        self._products = products

    def get_products(self):
        """
        Повертає копію списку продуктів.
        """
        return self._products.copy()

    def add_product(self, product):
        """
        Додає продукт до списку.
        """
        self._products.append(product)

    def remove_product(self, product_id):
        """
        Видаляє продукт зі списку за його ідентифікатором.
        """
        self._products = [product for product in self._products if product.get_product_id() != product_id]

    def print_product_details(self, product_id):
        """
        Виводить детальну інформацію про продукт за його ідентифікатором.
        """
        for product in self._products:
            if product.get_product_id() == product_id:
                print(f"Product ID: {product.get_product_id()}, Name: {product.get_name()}, Category: {product.get_category()}, Price: {product.get_price()}")