'''
A format for expressing an ordered list of integers is to use a comma separated list of either

individual integers
or a range of integers denoted by the starting integer separated from the end integer in the range by a dash, '-'. The range includes all integers in the interval including both endpoints. It is not considered a range unless it spans at least 3 numbers. For example "12,13,15-17"
Complete the solution so that it takes a list of integers in increasing order and returns a correctly formatted string in the range format.

Example:

solution([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])
# returns "-6,-3-1,3-5,7-11,14,15,17-20"
'''


def group(args):
    # First and last number of a sequence
    # A sequence example is: [-3, -2, -1], [1, 2, 3, 4, 5]
    first_num = last_num = args[0]
    for n in args[1:]:
        # Assign current value to last number for next loop
        if n - 1 == last_num:
            last_num = n
        # Stop if get biggest number of a sequence
        else:
            # Then check if first number == last number in sequence => return only a number
            if first_num == last_num:
                yield first_num
            # If sequence only has 2 number which is first and last number => just return both of them without '-'
            elif last_num - first_num == 1:
                yield first_num
                yield last_num
            # Other cases => return sequence with '-'
            else:
                yield f'{first_num}-{last_num}'
            first_num = last_num = n
    # Yield for the last value which not in for loop
    if first_num == last_num:
        yield first_num
    elif last_num - first_num == 1:
        yield first_num
        yield last_num
    else:
        yield f'{first_num}-{last_num}'

def solution(args):
    # Convert result of group func into list of str
    # then join
    return ','.join([str(i) for i in list(group(args))])