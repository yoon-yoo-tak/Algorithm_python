"""

9626 크로스워드 퍼즐

"""
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

u, l, r, d = map(int, input().split())

def cross(x, y):
    if (x + y) % 2 == 0:
        return '#'
    else:
        return '.'

c = [input().strip() for _ in range(n)]
f = [[] * 20 for _ in range(20)]

for i in range(n+u+d):
    for j in range(l+m+r):
        f[i][j] = cross(i, j)

for i in range(n):
    for j in range(m):
        f[i + u][j + l] = c[i][j]

for i in range(n + u + d):
    for j in range(l + m + r):
        print(f[i][j])
