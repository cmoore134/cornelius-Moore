class Number:
    def __init__(self, num):
        self.num = num

    def __str__(self):
        return str(self.num)

    def __add__(self, other):
        return Number(self.num + other.num)

    def __sub__(self, other):
        return Number(self.num - other.num)

    def __mul__(self, other):
        return Number(self.num * other.num)

    def __truediv__(self, other):
        return Number(self.num // other.num)
        
# Demonstration
num1 = Number(25)
num2 = Number(5)

# Addition
result_add = num1.__add__(num2)
print(f"{num1} + {num2} = {result_add}")

# Subtraction
result_sub = num1.__sub__(num2)
print(f"{num1} - {num2} = {result_sub}")

# Multiplication
result_mul = num1.__mul__(num2)
print(f"{num1} * {num2} = {result_mul}")

# Division
result_div = num1.__truediv__(num2)
print(f"{num1} / {num2} = {result_div}")

# Combination

num3 = Number(30)
num4 = Number(20)
num5 = Number(5)
num6 = Number(125)

result_combo = num3.__add__(num4.__mul__(num5)).__truediv__(num6)
print(f"( {num3} + {num4} * {num5} ) / {num6} = {result_combo}")