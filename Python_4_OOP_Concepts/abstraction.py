# Абстракция - это процесс скрытия деталей и предоставления только необходимых данных пользователю.

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.14 * self.radius
    
rectangle = Rectangle(10, 20)
circle = Circle(12)

print('Rectangle: P =', rectangle.perimeter(), '| A =', rectangle.area())
# Rectangle: P = 60 | A = 200
print('Circle: P =', circle.perimeter(), '| A =', circle.area())
# Circle: P = 75.36 | A = 452.16