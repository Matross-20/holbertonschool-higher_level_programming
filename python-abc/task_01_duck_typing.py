from abc import ABC, abstractmethod

class Shape(ABC):
  """Abstract base class for shapes."""

  @abstractmethod
  def area(self):
    """Calculates the area of the shape."""
    pass

  @abstractmethod
  def perimeter(self):
    """Calculates the perimeter of the shape."""
    pass

class Circle(Shape):
  """Concrete class representing a circle."""

  def __init__(self, radius):
    self.radius = radius

  def area(self):
    return 3.14159 * self.radius**2

  def perimeter(self):
    return 2 * 3.14159 * self.radius

class Rectangle(Shape):
  """Concrete class representing a rectangle."""

  def __init__(self, width, height):
    self.width = width
    self.height = height

  def area(self):
    return self.width * self.height

  def perimeter(self):
    return 2 * (self.width + self.height)

def shape_info(shape):
  """Prints the area and perimeter of a shape object."""
  print(f"Area: {shape.area()}")
  print(f"Perimeter: {shape.perimeter()}")

# Testing
circle = Circle(5)
rectangle = Rectangle(4, 3)

shape_info(circle)
shape_info(rectangle)
