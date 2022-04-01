"""
21918 전구

1. 아이디어
2. 시간복잡도
3. 자료구조
"""

import sys
input = sys.stdin.readline
n, m = map(int, input().split())
ls = list(map(int, input().split()))

def bulb(a, b, c):
    if a == 1:
        ls[b] = c
    elif a == 2:
        for i in range(b, c):
            if ls[i] == 0:
                ls[i] = 1
            else:
                ls[i] = 0
    elif a == 3:
        for i in range(b, c):
            ls[i] = 0
    else:
        for i in range(b, c):
            ls[i] = 1

for _ in range(m):
    a, b, c = map(int, input().split())
    bulb(a, b - 1, c)

print(*ls)

