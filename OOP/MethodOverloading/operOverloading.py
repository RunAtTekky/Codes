class OperatorOverloading:
    def __init__(self, x):
        self.x = x

    def __and__(self, other):
        return OperatorOverloading(self.x & other.x)

    def __or__(self, other):
        return OperatorOverloading(self.x | other.x)

    def __xor__(self, other):
        return OperatorOverloading(self.x ^ other.x)

    def __sub__(self, other):
        return OperatorOverloading(self.x - other.x)

    def __mul__(self, other):
        return OperatorOverloading(self.x * other.x)

    def __truediv__(self, other):
        if other.x == 0:
            raise ValueError("Division by zero is not allowed")
        return OperatorOverloading(self.x / other.x)

    def __str__(self):
        return str(self.x)

a = OperatorOverloading(5)
b = OperatorOverloading(3)

print(f'{a} <- a {b} <- b')

result_and = a & b
print(f'AND: {result_and}')

result_or = a | b
print(f'OR: {result_or}')

result_xor = a ^ b
print(f'XOR: {result_xor}')

result_sub = a - b
print(f'Subtraction: {result_sub}')

result_mul = a * b
print(f'Multiplication: {result_mul}')

result_div = a / b
print(f'Division: {result_div}')
