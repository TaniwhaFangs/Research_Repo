"""
SOLID principles

S: single-responsibility principle
O: open-closed principle
L: liskov segregation principle
I: interface segregation principle
D: dependency inversion principle

Single Responsibility Principle:
A class should have only one responsibility.

Open-Closed Principle:
Software entities should be open for expansion but closed to modification.

Liskov Substitution Principle:
Subtypes must be substitutable for their base types without breaking the code.

Interface Segregation Principle:
Similar to single responsibility principle. Clients should not be forced to depend upon methods that they do not use. Interfaces belong to clients, not to hierarchies.
  
Dependency Inversion Principle:
Abstractions should not depend upon details. Details should depend upon abstractions.

Below is an example of some code using turtle to create shapes that adheres to SOLID principles (This is not my code):

import turtle

# Base class for shapes
class Shape:
    def __init__(self, color):
        # Initialize a Turtle object for drawing
        self.t = turtle.Turtle()
        # Set the color of the shape
        self.t.color(color)
    def draw(self):
        # This method is abstract and will be overridden by subclasses
        pass
class pheobe(Shape):
    def __init__(self, color, side_length):
        super().__init__(color)
        self.side_length = side_length

    def draw(self):
        # Draw an equilateral triangle
        for _ in range(8):
            self.t.forward(self.side_length)
            self.t.left(45)
class Daniel(Shape):
    def __init__(self, color, side_length):
        super().__init__(color)
        self.side_length = side_length
    def draw(self):
        for i in range(15):
            self.t.forward(self.side_length)
            self.t.left(168)

# Circle class
class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def draw(self):
        # Draw a circle with the given radius
        self.t.circle(self.radius)
class star(Shape):
    def __init__(self, color, side_length):
        super().__init__(color)
        self.side_length = side_length
    def draw(self):
        for i in range(5):
            self.t.forward(self.side_length)
            self.t.left(36-180)
            self.t.forward(self.side_length)
            self.t.left(180-108)

class rhombus(Shape):
    def __init__(self, color, side_length):
        super().__init__(color)
        self.side_length = side_length
    def draw(self):
        for i in range(2):
            self.t.forward(self.side_length)
            self.t.left(45)
            self.t.forward(self.side_length)
            self.t.left(180-45)


myshape = Circle("blue", 100)
myshape.draw()
"""
