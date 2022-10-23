"""
1687 행렬 찾기
"""
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
matrix = [[0] * (m + 1)] + [[0] + list(map(int, input().strip())) for _ in range(n)]
prefix = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if matrix[i][j] == 0:
            prefix[i][j] = prefix[i - 1][j] + 1
ans = 0
for i in range(1, n + 1):
    for j in range(1, m + 1):
        temp = int(1e9)
        if prefix[i][j] == 0:
            continue
        for k in range(j, 0, -1):
            if prefix[i][k] < temp:
                temp = prefix[i][k]
            if (j - k + 1) * temp > ans:
                ans = (j - k + 1) * temp
print(ans)