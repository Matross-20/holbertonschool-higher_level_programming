from abc import ABC, abstractmethod
import math

# Define the abstract class Shape
class Shape(ABC):
    
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass

# Implement the Circle class with validation for negative radius
class Circle(Shape):
    def __init__(self, radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        self.radius = radius
    
    def area(self):
        return math.pi * (self.radius ** 2)
    
    def perimeter(self):
        return 2 * math.pi * self.radius

# Implement the Rectangle class
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

# Define the shape_info function
def shape_info(shape):
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")

# Test function for Circle with negative radius
def test_circle_negative():
    try:
        circle_negative = Circle(-5)
    except ValueError as e:
        print(e)

# Run the negative radius test
test_circle_negative()

# Additional tests to verify the main functionality
def run_tests():
    # Test with Circle
    print("Testing Circle with radius 5:")
    try:
        circle = Circle(5)
        shape_info(circle)
    except Exception as e:
        print(f"Test failed for Circle with error: {e}")

    # Test with Rectangle
    print("Testing Rectangle with width 4 and height 7:")
    try:
        rectangle = Rectangle(4, 7)
        shape_info(rectangle)
    except Exception as e:
        print(f"Test failed for Rectangle with error: {e}")

# Run the additional tests
run_tests()

