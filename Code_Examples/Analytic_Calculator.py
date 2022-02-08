""""
Author: Josh Wolfe

Quadratic formula calculator (Analytical Method)
"""
import math

# Takes input for a, b, and c from user
a = float(input('Please enter integer for a: '))
b = float(input('Please enter integer for b: '))
c = float(input('Please enter integer for c: '))

x1 = 0
x2 = 0

print('Solving ax^2 + bx + c = 0:')
print('a = ', a)
print('b = ', b)
print('c = ', c)

# Sets formula to a variable

quadratic_formula = (b ** 2) - (4 * a * c)

# Calculates the quadratic formula when the square root is greater than zero
if quadratic_formula > 0:
    x1 = ((-(b)) + math.sqrt(quadratic_formula)) / (2 * a)
    x2 = ((-(b)) - math.sqrt(quadratic_formula)) / (2 * a)
    print('Roots: ', x1, x2)

# Calculates the formula when the square root is zero
elif quadratic_formula == 0:
    x1 = ((-(b)) + math.sqrt(quadratic_formula)) / (2 * a)
    print('Only one root: ', x1)

# Cannot calculate the formula due to square root of negative number
elif quadratic_formula < 0:
    print('No roots. Square root of a negative number is undefined')
    
