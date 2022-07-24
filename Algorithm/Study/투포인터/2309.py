"""
2309 일곱 난쟁이
"""
import sys

input = sys.stdin.readline
ls = sorted([int(input()) for _ in range(9)])
find = sum(ls) - 100
l, r = 0, 8
nan = []
while l <= r:
    if find > ls[l] + ls[r]:
        l += 1
    elif find < ls[l] + ls[r]:
        r -= 1
    else:
        nan.append(ls[l])
        nan.append(ls[r])
        break

for i in ls:
    if i not in nan:
        print(i)

