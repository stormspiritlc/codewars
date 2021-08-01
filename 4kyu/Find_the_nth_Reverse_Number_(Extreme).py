'''
Reverse Number is a number which is the same when reversed.

For Example;
  0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101 => First 20 Reverse Numbers
  
TASK:
You need to return the nth reverse number. (Assume that reverse numbers start from 0 as shown in the example.)

NOTES:
1 < n <= 100000000000
'''


def find_reverse_number(n):
    # 10 numbers from 0-9
    if n <= 10:
        return n-1
    # 9 number from 11-99
    if n <= 19:
        return int(str(n-10)*2)
    # other cases
    else:
        # -1 to exlucde 0 and start from 1
        # then -1 more to set order start from 1, not 0
        n -= 2
        # set number of digits = 1
        k = 1
        # count reserve numbers with k-digit = 9*10**((k-1)//2)
        # loop to count number of digits (k) and position (n) of n-th number
        while n > 9*10**((k-1)//2):
            n -= 9*10**((k-1)//2)
            k += 1
    # length of symetric half of palindrome number
    print(n,k)
    length = (k+1)//2
    # split position n to list of digits
    ls = [int(x) for x in str(n)]
    num = ""
    # fill list of digits to avoid error when loop
    while len(ls) != length:
        ls.insert(0, 0)
    # loop to get final number
    for i in range(length-1, -1, -1):
        # middle digit(s) of number
        if i == length-1:
            # if number of digits of number is odd
            if k % 2 != 0:
                num = str(ls[i])
            # if number of digits of number is odd
            else:
                num = str(ls[i])*2
        # first and last digits of number
        elif i == 0:
            num = str(ls[i]+1)+num+str(ls[i]+1)
        # other digits
        else:
            num = str(ls[i])+num+str(ls[i])
    # convert to int
    return int(num)

# thuật toán là tìm số chữ số k của số thứ n, và vị trí của nó tính từ số palindrome đầu tiên với k chữ số
# số palindrome thứ n tính từ số palindrome đầu tiên với k chữ số có thể được tính bằng vị trí của nó
# chẳng hạn n ban đầu là 1001 -> k=5 và n=801 tính từ số palindrome đầu tiên có 5 chữ số (10001)
# 1 số palindrome 5 chữ số có dạng "xyzyx" với x=8+1, y=0, z=1 theo vị trí của nó
# => số đó là 90109