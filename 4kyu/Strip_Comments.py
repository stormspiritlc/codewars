'''
Complete the solution so that it strips all text that follows any of a set of comment markers passed in. Any whitespace at the end of the line should also be stripped out.

Example:
Given an input string of:
apples, pears # and bananas
grapes
bananas !apples

The output expected would be:
apples, pears
grapes
bananas

The code would be called like so:
result = solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
# result should == "apples, pears\ngrapes\nbananas"
'''


import re
def solution(string,markers):
    # split by line in string
    lines = string.split('\n')
    # create regex string from markers
    marker_regex = '|'.join(["\\"+marker for marker in markers])
    if marker_regex != "":
        # delete comment for each line
        new_lines = [re.split(fr'{marker_regex}', line)[0].rstrip(' ') for line in lines]
        # join into string again
        return "\n".join(new_lines)
    else: return "\n".join(lines)