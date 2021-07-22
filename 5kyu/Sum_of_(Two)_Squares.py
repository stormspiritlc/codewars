'''
Complete the function that takes a non-negative integer, and returns a list of non-negative integer pairs whose values - when squared - sum to the given integer.

For example, given the parameter 25, the function should return the two pairs [0, 5] and [3, 4] because 0^2 + 5^2 = 25 and 3^2 + 4^2 = 25.

Return the pairs in ascending order, so e.g. [[0, 5], [3, 4]] not [[5, 0], [3, 4]] or [[3, 4], [0, 5]], etc.

If the given value cannot be expressed as the sum of two squares, return an empty array.

Note: The upper bound of the parameter value will be 2,147,483,647

Examples
  0  -->  [ [0, 0] ]
  1  -->  [ [0, 1] ]
  2  -->  [ [1, 1] ]
  3  -->  []
  4  -->  [ [0, 2] ]
  5  -->  [ [1, 2] ]
 25  -->  [ [0, 5], [3, 4] ]
325  -->  [ [1, 18], [6, 17], [10, 15] ]
'''


import math
def all_squared_pairs(n):
    return sorted([list(x) for x in set(tuple(sorted(l)) for l in [[i, int(math.sqrt(n-i**2))] for i in range(int(math.sqrt(n))+1) if math.sqrt(n-i**2).is_integer()])], key=lambda x: x[0])

# Full form of function
def all_squared_pairs(n):
    ls, sorted_ls, final_ls = [], [], []
    # loop all number less than sqrt(n)
    for i in range(int(math.sqrt(n))+1):
        # find remain number
        j = math.sqrt(n-i**2)
        # check if the remain number is integer or not
        # if true => append to list ls
        if j.is_integer():
            ls.append([i, int(j)])
    # sort ls and convert to list of tuples
    for l in ls:
        sorted_ls.append(tuple(sorted(l)))
    # then use set() to remove duplicate tuples
    # convert tuples to list again then append to final_ls
    for x in set(sorted_ls):
        final_ls.append(list(x))
    # sort final_ls last time to match requirement
    return sorted(final_ls, key=lambda x: x[0])


