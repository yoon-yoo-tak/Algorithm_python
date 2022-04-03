"""


1. 아이디어
2. 시간복잡도
3. 자료구조
"""

import sys

input = sys.stdin.readline

n = int(input(0))

a = [list(map(int, input().split())) for _ in range(n)]

v, I, J = 0, 0, 0
for i in range(n):
    for j in range(n):
        if a[i][j] > v:
            v = a[i][j]
            I, J = i, j

def solve(first):
    ord = [(a[first][i] , i) for i in range(n)]
    ord.sort()
    for dist, idx in ord:
        print(idx + 1, end=' ')
    print()

solve(I)
solve(J)