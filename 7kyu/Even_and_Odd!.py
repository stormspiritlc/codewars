'''
Given a number N, can you fabricate two numbers NE and NO such as NE is formed by even digits of N and NO is formed by odd digits of N? Examples:

126453 -> NE = 264, NO = 153
3012 -> NE = 2, NO = 31
4628 -> NE = 4628, NO = 0 0 is considered as an even number.
In C you should return an array of two elements such as the first is NE and the second is NO.
'''


def even_and_odd(n):
    return tuple([int(i) if i else 0 for i in [''.join([i  for i in str(n) if int(i) % 2 == 0]), ''.join([i  for i in str(n) if int(i) % 2 != 0])]])