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
    if n <= 10:
        return n-1
    if n <= 19:
        return int(str(n-10)*2)
    else:
        n -= 1
        k = 1
        while n > 9*10**((k-1)//2):
            n -= 9*10**((k-1)//2)
            k += 1
    n-=1
    length = (k+1)//2
    ls = [int(x) for x in str(n)]
    num = ""
    while len(ls) != length:
        ls.insert(0, 0)
    for i in range(length-1, -1, -1):
        if i == length-1:
            if k % 2 != 0:
                num = str(ls[i])
            else:
                num = str(ls[i])*2
        elif i == 0:
            num = str(ls[i]+1)+num+str(ls[i]+1)
        else:
            num = str(ls[i])+num+str(ls[i])
    return int(num)