"""
2669 직사각형 네개의 합집합의 면적 구하기
"""

import sys

input = sys.stdin.readline
ls = [[0] * 100 for _ in range(100)]
for i in range(4):
    a, b, c, d = map(int, input().split())
    for i in range(a, c):
        for j in range(b, d):
            ls[i][j] = 1
ans = 0
for i in ls:
    ans += sum(i)

print(ans)
