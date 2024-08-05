from abc import ABC, abstractmethod
import math

class Shape(ABC):
    """Abstract base class for shapes."""

    @abstractmethod
    def area(self):
        """Calculate the area of the shape.

        Returns:
            float: The area of the shape.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate the perimeter of the shape.

        Returns:
            float: The perimeter of the shape.
        """
        pass

class Circle:
    def __init__(self, radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        self.radius = radius
        
    def perimeter(self):
        return 2 * 3.141592653589793 * self.radius

    def area(self):
        return 3.141592653589793 * (self.radius ** 2)

class Rectangle(Shape):
    """Class representing a rectangle, inheriting from Shape."""

    def __init__(self, width, height):
        """Initialize a Rectangle with a given width and height.

        Args:
            width (float): The width of the rectangle.
            height (float): The height of the rectangle.
        """
        self.width = width
        self.height = height

    def area(self):
        """Calculate the area of the rectangle.

        Returns:
            float: The area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """Calculate the perimeter of the rectangle.

        Returns:
            float: The perimeter of the rectangle.
        """
        return 2 * (self.width + self.height)

def shape_info(shape):
    """Print the area and perimeter of a shape.

    Args:
        shape (Shape): An object that has area and perimeter methods.
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")

# Example usage:
if __name__ == "__main__":
    circle = Circle(5)
    rectangle = Rectangle(4, 7)

    print("Circle:")
    shape_info(circle)  # Should print the area and perimeter of the circle

    print("\nRectangle:")
    shape_info(rectangle)  # Should print the area and perimeter of the rectangle
