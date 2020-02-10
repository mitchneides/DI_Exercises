import math


class Circle:
    def __init__(self, radius=1.0):
        self.radius = radius

    def get_perimeter(self):
        perimeter = 2 * math.pi * self.radius
        print(perimeter)
        return perimeter

    def get_area(self):
        area = math.pi * self.radius**2
        print(area)
        return area


circle1 = Circle(3)
circle1.get_perimeter()
circle1.get_area()








