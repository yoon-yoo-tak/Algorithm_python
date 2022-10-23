"""
11660 구간 합 구하기 5
"""
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
prefix_sum = [[0] * (n + 1) for _ in range(n + 1)]
ls = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        prefix_sum[i + 1][j + 1] = prefix_sum[i][j + 1] + prefix_sum[i + 1][j] - prefix_sum[i][j] + ls[i][j]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    print(prefix_sum[x2][y2] - prefix_sum[x1 -1][y2] - prefix_sum[x2][y1 - 1] + prefix_sum[x1 - 1][y1 - 1])