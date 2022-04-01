"""
9358 순열 접기 게임

1. 아이디어
2. 시간복잡도
3. 자료구조
"""

import sys

input = sys.stdin.readline
t = int(input())

for i in range(t):
    n = int(input())
    ls = list(map(int, input().split()))
    while True:
        if len(ls) == 2:
            if ls[0] > ls[1]:
                print('Case #%d: Alice'%(i + 1))
            else:
                print('Case #%d: Bob'%(i + 1))
            break
        if len(ls) % 2 == 0:
            for j in range(len(ls) // 2):
                ls[j] += ls[len(ls) - 1 - j]
            for _ in range(len(ls) // 2):
                ls.pop()
        else:
            for j in range(len(ls) // 2 + 1):
                ls[j] += ls[len(ls) - 1 - j]
            for _ in range(len(ls) // 2):
                ls.pop()