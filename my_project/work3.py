import math

# 基类 Figure
class Figure:
    def area(self):
        pass

    def perimeter(self):
        pass

    def compare_area(self, other):
        if self.area() > other.area():
            return "больше"
        elif self.area() < other.area():
            return "меньше"
        else:
            return "равно"

    def compare_perimeter(self, other):
        if self.perimeter() > other.perimeter():
            return "больше"
        elif self.perimeter() < other.perimeter():
            return "меньше"
        else:
            return "равно"

# 正方形类
class Square(Figure):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side

# 矩形类
class Rectangle(Figure):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

# 三角形类
class Triangle(Figure):
    def __init__(self, a, b,c):
        self.a = a
        self.b = b
        self.c = c
        self.d = (a + b + c) / 2
    def area(self):
        return math.sqrt(self.d*(self.d - self.a)*(self.d-self.b)*(self.d - self.c))

    def perimeter(self):
        return self.a + self.b + self.c
# 圆形类
class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius

# test
square = Square(4)
rectangle = Rectangle(3, 4)
triangle = Triangle(3, 4, 5)
circle = Circle(3)

print("s1:", square.area())
print("l1:", square.perimeter())
print("compare area", square.compare_area(circle))
print("compare perimeter", square.compare_perimeter(circle))
print("compare area", square.compare_area(triangle))