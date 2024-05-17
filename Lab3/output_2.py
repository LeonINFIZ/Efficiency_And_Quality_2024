class ShapeCalculator:
    def calculate_area(self, shape):
        return shape.calculate_area()

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius * self.radius

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5 * self.base * self.height

# Приклад використання класу
calculator = ShapeCalculator()

circle = Circle(5)
circle_area = calculator.calculate_area(circle)
print("Area of circle:", circle_area)

rectangle = Rectangle(4, 6)
rectangle_area = calculator.calculate_area(rectangle)
print("Area of rectangle:", rectangle_area)

triangle = Triangle(3, 8)
triangle_area = calculator.calculate_area(triangle)
print("Area of triangle:", triangle_area)