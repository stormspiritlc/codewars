# DESCRIPTION

# Given an array of positive or negative integers
# I= [i1,..,in]
# you have to produce a sorted array P of the form
# [ [p, sum of all ij of I for which p is a prime factor (p positive) of ij] ...]
# P will be sorted by increasing order of the prime numbers. The final result has to be given as a string in Java, C#, C, C++ and as an array of arrays in other languages.

# Example:
# I = [12, 15] # result = [[2, 12], [3, 27], [5, 15]]
# [2, 3, 5] is the list of all prime factors of the elements of I, hence the result.

# Notes:
# It can happen that a sum is 0 if some numbers are negative!
# Example: I = [15, 30, -45] 5 divides 15, 30 and (-45) so 5 appears in the result, the sum of the numbers for which 5 is a factor is 0 so we have [5, 0] in the result amongst others.



# SOLUTION
import math
def get_prime(lst):
    ls = []
    for n in lst:
        # turn into positive number that can be squared root
        n = abs(n)
        while n % 2 == 0:
            ls.append(2)
            n = n / 2
        for i in range(3,int(math.sqrt(n))+1,2):
            while n % i== 0:
                ls.append(int(i))
                n = n / i
        if n > 2:
            ls.append(int(n))
    # return list of all prime factors of all number in lst
    return ls

def sum_for_list(lst):
    # remove duplicate factors in ls
    ls = list(dict.fromkeys(get_prime(lst)))
    # sort them
    ls.sort()
    # sum all number i in lst if i can divide to j for each j in list of prime factors
    return [[j, sum([i for i in lst if i % j == 0])] for j in ls]