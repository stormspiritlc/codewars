'''
Consider the sequence U(n, x) = x + 2x**2 + 3x**3 + .. + nx**n where x is a real number and n a positive integer.
When n goes to infinity and x has a correct value (ie x is in its domain of convergence D), U(n, x) goes to a finite limit m depending on x.
Usually given x we try to find m. Here we will try to find x (x real, 0 < x < 1) when m is given (m real, m > 0).
Let us call solve the function solve(m) which returns x such as U(n, x) goes to m when n goes to infinity.

Examples:
solve(2.0) returns 0.5 since U(n, 0.5) goes to 2 when n goes to infinity.
solve(8.0) returns 0.7034648345913732 since U(n, 0.7034648345913732) goes to 8 when n goes to infinity.

Note:
You pass the tests if abs(actual - expected) <= 1e-12
'''

import math
def solve(m):
    return (2+1/m+math.sqrt(4/m+1/m**2))/2

# U(n,x) = x(x^n-1)/x-1 + xU(n-1,x)
# n->infinity = a => a = (x^n-1)/x-1 + xa
# if x>1 => x^n->infinity => to remove x^n, x<1, then x^n=0
# => a(1-x) = -1/x-1 => x^2-(2+1/a)x+a = 0
# => x = (2+1/a+-sqrt(4/a+1/a^2))/2, but x<1 => x = (2+1/a-sqrt(4/a+1/a^2))/2
# apply to code