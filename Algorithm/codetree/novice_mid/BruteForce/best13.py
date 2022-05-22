"""
최고의 13 위치
"""
import sys

input = sys.stdin.readline

n = int(input())
ls = [list(map(int, input().split())) for _ in range(n)]

cnt = -1
for i in range(n):
    for j in range(n - 2):
        cnt = max(cnt, ls[i][j] + ls[i][j + 1] + ls[i][j + 2])

print(cnt)