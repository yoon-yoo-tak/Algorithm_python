"""
11497 통나무 건너뛰기

"""

import sys
from collections import deque
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    ls = sorted(map(int, input().split()))
    temp = deque()
    while ls:
        temp.appendleft(ls.pop())
        if ls:
            temp.append(ls.pop())
    temp = list(temp)
    ans = -1
    for i in range(len(temp)):
        next = i + 1
        if next == len(temp):
            next = 0
        ans = max(ans, abs(temp[i] - temp[next]))
    print(ans)