"""
Author: Josh Wolfe

Quadratic formula calculator (Newton-Raphson Method)
"""

import math
import random

# Takes input for a, b, and c from user
a = float(input('Please enter integer for a: '))
b = float(input('Please enter integer for b: '))
c = float(input('Please enter integer for c: '))

print('Solving ax^2 + bx + c = 0:')
print('a = ', a)
print('b = ', b)
print('c = ', c)

# Sets quadratic formula to a variable
quadratic_formula = (b ** 2) - (4 * a * c)

# Initiates variables
epsilon = 0.0000000001
k = quadratic_formula
guess = random.randint(-100,100)
guess_count = 0

# Detects if roots exist
# If roots exist, branch executes
if (b ** 2) >= (4 * a * c):
    print('At least one root exists. Calclulating:')
    inital_guess = guess
    while abs(guess -(guess - (a * guess ** 2 + b * guess + c) / (2 * a * guess + b))) >= epsilon:
        guess_count += 1
        guess = guess - (a * guess ** 2 + b * guess + c) / (2 * a * guess + b)
     
    print('Square root is about: ', guess)
else:
    print('No roots available. Program Stopped')
print('Initial guess was :', inital_guess)
print('Number of guess iterations: ', guess_count)
