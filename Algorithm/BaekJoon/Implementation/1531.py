"""
1531 투명
"""
import sys
input = sys.stdin.readline
paint = [[0] * 100 for _ in range(100)]
n, m = map(int, input().split())
for _ in range(n):
    a, b, c, d = map(int, input().split())
    for i in range(a, c + 1):
        for j in range(b, d + 1):
            paint[i - 1][j - 1] += 1
cnt = 0
for i in range(100):
    for j in range(100):
        if paint[i][j] > m:
            cnt += 1
print(cnt)