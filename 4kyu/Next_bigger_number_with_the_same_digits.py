# DESCRIPTION

# Create a function that takes a positive integer and returns the next bigger number that can be formed by rearranging its digits. For example:

# 12 ==> 21
# 513 ==> 531
# 2017 ==> 2071
# nextBigger(num: 12)   // returns 21
# nextBigger(num: 513)  // returns 531
# nextBigger(num: 2017) // returns 2071
# If the digits can't be rearranged to form a bigger number, return -1 (or nil in Swift):

# 9 ==> -1
# 111 ==> -1
# 531 ==> -1
# nextBigger(num: 9)   // returns nil
# nextBigger(num: 111) // returns nil
# nextBigger(num: 531) // returns nil



# SOLUTION
def next_bigger(num):
    # get length of number string
    n = len(str(num))
    # split number into list of digits
    ls = [int(x) for x in str(num)]
    # find the location that need to rearrange
    i = 0
    while ls[n-i-2] >= ls[n-i-1]:
        if n-i-2 < 0:
            break
        else:
            i += 1
    # if number can't be rearrange into a bigger number
    if n-i-2 < 0:
        return -1
    # normal case
    else:
        # sub list of digits that need to rearrange
        ## first digit
        first_digit = ls[n-i-2]
        ## sub list except first_digit
        sub_ls = ls[n-i-1:]
        # find smallest value in sublist that higher than first_digit
        # then swap with first_digit
        val = min(i for i in sub_ls if i > first_digit)
        sub_ls.remove(val)
        sub_ls.append(ls[n-i-2])
        # sort sub list to get the smallest
        sub_ls.sort()
        # concat original list, new value after swap, and sub list after sort
        ls = ls[:n-i-2] + [val] + sub_ls
        # convert list into number
        string_ints = [str(int) for int in ls]
        str_of_ints = "".join(string_ints)
        return int(str_of_ints)