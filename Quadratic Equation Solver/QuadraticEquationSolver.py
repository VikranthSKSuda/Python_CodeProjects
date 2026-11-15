import math

print("This Program Solves the Quadratic Equation And Tells You the amount of zeros:")

a = int(input("A: ")) #Need to use values from standard form
b = int(input("B: "))
c = int(input("C: "))

_2a = 2 * a                                    #Denominator
_bsquared = b ** 2                                
_4ac = 4 * a * c
discrimintant = _bsquared - _4ac                #Discriminant Value Stored
numerator_pos = -b + math.sqrt(discrimintant)
numerator_neg = -b - math.sqrt(discrimintant)

if discrimintant < 0:
    print("No x-ints")
    print("No Solution")
elif discrimintant == 0:
    value_1 = -b / _2a
    print("1 x-ints")
    print(f"There is only one value and it is {value_1}.")
elif discrimintant > 0:
    value_1 = numerator_pos/_2a
    value_2 = numerator_neg/_2a
    print("2 x-ints")
    print(f"The 2 values are {value_1} and {value_2}.")
