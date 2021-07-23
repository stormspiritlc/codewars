'''
This is my republished first kata(with issues fixed!), hope you guys will enjoy it!

For input, you will be given a string in the form "(mx+n)(px+q)" where the character x can be any single lowercase alphabet from a-z, while m, n, p and q are integers(can be negative).

Task
Return a string in the format ax^2+bx+c where a, b and c are integers, eg. 5x^2-6x+8
If a or b is 1, the '1' in front of the variable should be omitted. eg. x^2+x-20
If a or b is -1, only the minus sign - should be shown, eg. -x^2-x+6
Examples:
quadratic_builder("(x+2)(x+3)")  #return "x^2+5x+6"
quadratic_builder("(x-2)(x+7)")  #return "x^2+5x-14"
quadratic_builder("(3y+2)(y+5)")  #return "3y^2+17y+10"
quadratic_builder("(-h-7)(4h+3)")  #return "-4h^2-31h-21"
'''


import re
def quadratic_builder(expression):
    ls = ' '.join(re.split(r'\(|\)', expression)).split()
    ls_num = []
    for i in ls:
        # extract variable
        word = ''.join(j for j in i if j.isalpha())
        # extract all coefficients
        ls_num += i.split(word)
    # replace to number in case 1 or -1 is not shown
    ls_num = [1 if j == '' else -1 if j == '-' else int(j) for j in ls_num]
    # count coefficients of output equation
    first_param = ls_num[0]*ls_num[2]
    second_param = ls_num[0]*ls_num[3]+ls_num[1]*ls_num[2]
    third_param = ls_num[1]*ls_num[3]
    # replace again if number is 1 or -1
    first_param = '' if (first_param == 1) else '-' if (first_param  == -1) else first_param
    second_param = '' if (second_param == 1) else '-' if (second_param  == -1) else second_param
    # check if a coefficient = 0 then remove both coefficient+variable
    word = ""
    if first_param != 0:
        word += f'{first_param}{word}^2'
    if second_param != 0:
        word += f'+{second_param}{word}'
    if third_param != 0:
        word += f'+{ls_num[1]*ls_num[3]}'
    # replace +- by - to have shortest result
    return word.replace('+-', '-')
