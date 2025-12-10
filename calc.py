import math

class Calc:
    def __init__(self):
        self.memory = 0.0

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Деление на ноль невозможно")
        return a / b

    def modulo(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Деление на ноль невозможно")
        return a % b

    def sin(self, a):
        return math.sin(math.radians(a))

    def cos(self, a):
        return math.cos(math.radians(a))

    def power(self, a, b):
        return a ** b

    def sqrt(self, a):
        if a < 0:
            raise ValueError("Нельзя взять корень из отрицательного числа")
        return math.sqrt(a)

    def floor(self, a):
        return math.floor(a)

    def ceil(self, a):
        return math.ceil(a)



