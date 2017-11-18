import figure
from math import sqrt


class triangle(figure.figure):
    def __init__(self, side_a, side_b, side_c):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def perimeter(self):
        return self.side_a + self.side_b + self.side_c

    def area(self):
        half_p = self.perimeter() / 2
        return sqrt(half_p * (half_p - self.side_a) * (half_p - self.side_b) * (half_p - self.side_c))
