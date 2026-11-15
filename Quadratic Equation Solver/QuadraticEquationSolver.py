import math

print("This Program Solves the Quadratic Equation And Tells You the amount of zeros:")

a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))

_2a = 2 * a
_bsquared = b ** 2
_4ac = 4 * a * c
discrimintant = _bsquared - _4ac
numerator_pos = -b + math.sqrt(discrimintant)
numerator_neg = -b - math.sqrt(discrimintant)

if discrimintant < 0:
    print("No x-ints")
    print("No Solution")
