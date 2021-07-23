'''
1, 246, 2, 123, 3, 82, 6, 41 are the divisors of number 246. Squaring these divisors we get: 1, 60516, 4, 15129, 9, 6724, 36, 1681. The sum of these squares is 84100 which is 290 * 290.

Task
Find all integers between m and n (m and n integers with 1 <= m <= n) such that the sum of their squared divisors is itself a square.

We will return an array of subarrays or of tuples (in C an array of Pair) or a string. The subarrays (or tuples or Pairs) will have two elements: first the number the squared divisors of which is a square and then the sum of the squared divisors.

Example:
list_squared(1, 250) --> [[1, 1], [42, 2500], [246, 84100]]
list_squared(42, 250) --> [[42, 2500], [246, 84100]]
'''


from math import sqrt
def list_squared(m, n):
    result = []
    for num in range(m, n):
        divisors = set()
        for i in range(1, int(sqrt(num)+1)):
            if num % (i) == 0:
                # add divisors to set of divisors
                # then square all of them
                divisors.add(i**2)
                divisors.add(int(num/i)**2)
        # check if square root is integer
        if sqrt(sum(divisors)).is_integer():
            result += [[num, sum(divisors)]]
    return result
