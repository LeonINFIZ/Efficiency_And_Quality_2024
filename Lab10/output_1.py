class BasicCalculator:
    def add(self, a, b):
        """
        Додає два числа.
        """
        return a + b

    def subtract(self, a, b):
        """
        Віднімає одне число від іншого.
        """
        return a - b

    # Калькулятор не має методів для множення та ділення

class AdvancedCalculator(BasicCalculator):
    """
    Розширений калькулятор з додатковими методами.
    """
    def multiply(self, a, b):
        """
        Множить два числа.
        """
        return a * b

    def divide(self, a, b):
        """
        Ділить одне число на інше.
        """
        if b == 0:
            raise ZeroDivisionError("Ділення на нуль неможливе.")
        return a / b

calculator = AdvancedCalculator()
print("Addition:", calculator.add(5, 3))
print("Subtraction:", calculator.subtract(5, 3))
print("Multiplication: ", calculator.multiply(5, 3)) 
print("Division: ", calculator.divide(5, 3)) 