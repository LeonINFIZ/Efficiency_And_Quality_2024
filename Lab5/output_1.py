class ProductSearcher:
    """
    Відповідає за пошук товарів.
    """
    def search(self, query):
        # Пошук товару за запитом
        print(f"Пошук товарів за запитом: {query}")


class ProductDisplayer:
    """
    Відповідає за відображення інформації про товари.
    """
    def display(self, product):
        # Відображення інформації про товар
        print(f"Відображення товару: {product}")


class ProductOrderer:
    """
    Відповідає за замовлення товарів.
    """
    def order(self, product, quantity):
        # Замовлення товару
        print(f"Замовлення товару: {product}, кількість: {quantity}")


class Product:
    def __init__(self, name, price, type):
        self.name = name
        self.price = price
        self.type = type


# Приклад використання
searcher = ProductSearcher()
displayer = ProductDisplayer()
orderer = ProductOrderer()

product = Product("Laptop", 1000, "electronics")

searcher.search("laptop")
displayer.display(product)
orderer.order(product, 1)