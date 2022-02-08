""""
Author: Josh Wolfe

Quadratic formula calculator (Bisection Method)
"""

import math

# Takes input for a, b, c, high, and low from user
a = float(input('Please enter integer for a: '))
b = float(input('Please enter integer for b: '))
c = float(input('Please enter integer for c: '))
print('Please enter two initial values (integers) for x')
hi = float(input('Positive value for x: '))
lo = float(input('Negative value for x: '))

print('Solving ax^2 + bx + c = 0:')
print('a = ', a)
print('b = ', b)
print('c = ', c)
print('low bracket = ', lo)
print('high bracket = ', hi)

# Sets quadratic formula to a variable
quadratic_formula = (b ** 2) - (4 * a * c)

# Initializes variables
mid = (hi + lo) / 2.0
guess_count = 0
epsilon = 0.1
ans = 0


# Detects if function has two roots
# If function has less than two roots it prints out an error
if (b ** 2) > (4 * a * c):
    print('Two roots possible')
    while abs(ans - math.sqrt(quadratic_formula)) >= epsilon:
        guess_count += 1
        if mid ** 2 < hi:
            lo = mid
        else:
            hi = mid
        mid = (hi + lo) / 2.0
        ans = mid ** 2
    print('One square root is about: ', ans)
          
else:
    print('Function has less than two roots')
print('Took', guess_count, 'iterations')
