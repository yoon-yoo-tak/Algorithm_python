"""

2992 크면서 작은수

주어진 x를 이루는 모든 수에 대한 순열 구하고 그중 x보다 큰 수중 가장 작은수를 출력하면 되겠다.

X 자릿수가 최대 6자리.
백트래킹 가능.
"""
import sys
from itertools import permutations
input = sys.stdin.readline
ls = []
a = int(input())
perm = permutations(str(a), len(str(a)))
for i in perm:
    b = "".join(i)
    if int(b) > a:
        ls.append(int(b))

if len(ls) > 0:
    ls.sort()
    print(ls[0])
else:
    print(0)

