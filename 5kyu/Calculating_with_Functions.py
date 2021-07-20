'''
This time we want to write calculations using functions and get the results. Let's have a look at some examples:

seven(times(five())) # must return 35
four(plus(nine())) # must return 13
eight(minus(three())) # must return 5
six(divided_by(two())) # must return 3

Requirements:
There must be a function for each number from 0 ("zero") to 9 ("nine")
There must be a function for each of the following mathematical operations: plus, minus, times, dividedBy (divided_by in Ruby and Python)
Each calculation consist of exactly one operation and two numbers
The most outer function represents the left operand, the most inner function represents the right operand
Division should be integer division. For example, this should return 2, not 2.666666...:
'''


def zero(func = None): return func(0) if func!=None else 0
def one(func = None): return func(1) if func!=None else 1
def two(func = None): return func(2) if func!=None else 2
def three(func = None): return func(3) if func!=None else 3
def four(func = None): return func(4) if func!=None else 4
def five(func = None): return func(5) if func!=None else 5
def six(func = None): return func(6) if func!=None else 6
def seven(func = None): return func(7) if func!=None else 7
def eight(func = None): return func(8) if func!=None else 8
def nine(func = None): return func(9) if func!=None else 9

def plus(x): return lambda y: y+x
def minus(x): return lambda y: y-x
def times(x): return lambda y: y*x
def divided_by(x): return lambda y: y//x