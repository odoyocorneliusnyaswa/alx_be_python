import math

class Shape:
    """Base class representing a geometric shape"""
    
    def area(self):
        """Calculate the area of the shape (to be overridden by subclasses)"""
        raise NotImplementedError("Subclasses must implement this method")


class Rectangle(Shape):
    """Derived class representing a rectangle"""
    
    def __init__(self, length: float, width: float):
        """
        Initialize a rectangle with length and width
        Args:
            length (float): Length of the rectangle
            width (float): Width of the rectangle
        """
        self.length = length
        self.width = width
    
    def area(self):
        """Calculate the area of the rectangle (length × width)"""
        return self.length * self.width


class Circle(Shape):
    """Derived class representing a circle"""
    
    def __init__(self, radius: float):
        """
        Initialize a circle with radius
        Args:
            radius (float): Radius of the circle
        """
        self.radius = radius
    
    def area(self):
        """Calculate the area of the circle (π × radius²)"""
        return math.pi * (self.radius ** 2)
