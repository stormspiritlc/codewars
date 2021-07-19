'''
Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]
'''


def move_zeros(array):
    arr1, arr2 = [], []
    # assign non-zero values to arr1, and zeros to arr2
    for i, j in enumerate(array):
        if j != 0:
            arr1.append(j)
        else:
            arr2.append(0)
    # join them again
    return arr1+arr2