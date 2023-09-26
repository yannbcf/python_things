from typing import List, Union
import math

number = Union[int, float]

class Shape:
    def calculate_area(self) -> float:
        pass

class Circle(Shape):
    def __init__(self, radius: number):
        self.radius = radius

    def calculate_area(self) -> number:
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width: number, height: number):
        self.width = width
        self.height = height

    def calculate_area(self) -> number:
        return self.width * self.height

def total_area(shapes: List[Shape]) -> number:
    area = 0

    for shape in shapes:
        area += shape.calculate_area()

    return area

if __name__ == "__main__":
    circle_1 = Circle(5)
    circle_2 = Circle(3)
    rectangle = Rectangle(4, 6)

    print(f"Area of the circle 1: {circle_1.calculate_area():.2f} square units")
    print(f"Area of the circle 2: {circle_2.calculate_area():.2f} square units")
    print(f"Area of the rectangle: {rectangle.calculate_area()} square units")

    total = total_area([circle_1, rectangle, circle_2])
    print(f"Total area of all shapes: {total:.2f} square units")
