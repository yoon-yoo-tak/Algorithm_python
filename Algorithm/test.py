import sys
from collections import deque
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    f = sum(list(map(int, input().split())))
    day = 1
    while n >= f:
        day += 1
        f *= 4
    print(day)

