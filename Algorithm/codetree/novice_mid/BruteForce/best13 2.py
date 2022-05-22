"""
최고의 13위치 2
"""
import sys

input = sys.stdin.readline


n = int(input())
ls = [list(map(int, input().split())) for _ in range(n)]
ans = 0
for i in range(n):
    for j in range(n - 2):
        for k in range(n):
            for l in range(n - 2):
                if i == k and abs(j - l) <= 2:
                    continue
                ans = max(ans, ls[i][j] + ls[i][j + 1] + ls[i][j + 2] + ls[k][l] + ls[k][l + 1] + ls[k][l + 2])
print(ans)
