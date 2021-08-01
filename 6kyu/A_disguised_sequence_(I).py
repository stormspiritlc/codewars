'''
Given u0 = 1, u1 = 2 and the relation 6unun+1-5unun+2+un+1un+2 = 0 calculate un for any integer n >= 0.

Examples:
Call fcn the function such as fcn(n) = un.
fcn(17) -> 131072; fcn(21) -> 2097152

Remark:
You can take two points of view to do this kata:
the first one purely algorithmic from the definition of un
the second one - not at all mandatory, but as a complement - is to get a bit your head around and find which sequence is hidden behind un.
'''


def fcn (n):
    print(n)
    ls = []
    for i in range(n+1):
        if i == 0:
            ls.append(1)
        elif i == 1:
            ls.append(2)
        else:
            ls.append(round(6*ls[i-2]*ls[i-1]//(5*ls[i-2]-ls[i-1])))
    return ls[-1]