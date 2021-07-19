# DESCRIPTION

# Write a function that accepts two square (NxN) matrices (two dimensional arrays), and returns the product of the two. Only square matrices will be given.

# How to multiply two square matrices:
# We are given two matrices, A and B, of size 2x2 (note: tests are not limited to 2x2). Matrix C, the solution, will be equal to the product of A and B. To fill in cell [0][0] of matrix C, you need to compute: A[0][0] * B[0][0] + A[0][1] * B[1][0].
# More general: To fill in cell [n][m] of matrix C, you need to first multiply the elements in the nth row of matrix A by the elements in the mth column of matrix B, then take the sum of all those products. This will give you the value for cell [m][n] in matrix C.

# Example
#   A         B          C
# |1 2|  x  |3 2|  =  | 5 4|
# |3 2|     |1 1|     |11 8|



# SOLUTION
def matrix_mult(a, b):
    c = [([0]*len(a[0])) for i in range(len(a))]
    for m in range(len(c)):
        for n in range(len(c[0])):
            for t in range(len(c[0])):
                c[m][n] += a[m][t]*b[t][n]
    return c