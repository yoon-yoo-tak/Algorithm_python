"""
3040 백설 공주와 일곱 난장이

"""

import sys
from itertools import permutations
input = sys.stdin.readline
ls = [int(input()) for _ in range(9)]

perm = permutations(ls, 7)
for i in perm:
    if sum(i) == 100:
        for j in i:
            print(j)
        break
