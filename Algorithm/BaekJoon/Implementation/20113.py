"""

20113 긴급 회의

"""
import sys
input = sys.stdin.readline
n = int(input())
ls = list(map(int, input().split()))
tmp = [0] * (n + 1)
for i in ls:
    if i == 0:
        continue
    tmp[i] += 1
dead = max(tmp)


if tmp.count(dead) >= 2:
    print('skipped')
else:
    print(tmp.index(dead) if tmp.index(dead) != 0 else 'skipped')