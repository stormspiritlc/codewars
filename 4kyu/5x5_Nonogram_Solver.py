#     1   1
# 0   0   0
# 2   1   1

clues = (((1, 1), (4,), (1, 1, 1), (3,), (1,)),
          ((1,), (2,), (3,), (2, 1), (4,)))

# import numpy as np
ans = ((0, 0, 1, 0, 0),
       (1, 1, 0, 0, 0),
       (0, 1, 1, 1, 0),
       (1, 1, 0, 1, 0),
       (0, 1, 1, 1, 1))

sample = [[0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]]
# for i in range(len(clues)):
#     for j, value in enumerate(clues[i]):
#         if i == 0:
#             print()

clue = (4,1,1)
ls = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

def structure(clue):
    sample = []
    for index, val in enumerate(clue):
        while val >= 1:
            sample.append(1)
            val -= 1
        if index != len(clue)-1:
            sample.append(0)
    return sample
a = []
# a += [[0]*4]
# print(a)
sample = structure(clue)
num_0 = len(ls)-len(sample)

a += [0]*num_0
print(a)
