"""
2194 유닛 이동시키기
"""

import sys
from collections import deque
input = sys.stdin.readline

n, m, a, b, k = map(int, input().split())
li = [[0] * m for _ in range(n)]
get_value = lambda x: int(x) - 1
for _ in range(k):
    x, y = map(get_value, input().split())
    li[x][y] = 1
sx, sy = map(get_value, input().split())
ex, ey = map(get_value, input().split())

sum_li = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    temp = 0
    for j in range(1, m + 1):
        temp += li[i - 1][j - 1]
        sum_li[i][j] = temp + sum_li[i - 1][j]


def bfs():
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    dists = [[-1] * m for _ in range(n)]
    dists[sx][sy] = 0

    queue = deque()
    queue.append((sx, sy))
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx_s = x + dx[i]
            ny_s = y + dy[i]
            if nx_s < 0 or nx_s >= n or ny_s < 0 or ny_s >= m:
                continue
            nx_e = nx_s + a - 1
            ny_e = ny_s + b - 1
            if nx_e < 0 or nx_e >= n or ny_e < 0 or ny_e >= m:
                continue
            if dists[nx_s][ny_s] != -1:
                continue
            if sum_li[nx_e + 1][ny_e + 1] - sum_li[nx_s][ny_e + 1] - sum_li[nx_e + 1][ny_s] + sum_li[nx_s][ny_s] >= 1:
                continue
            dists[nx_s][ny_s] = dists[x][y] + 1
            if nx_s == ex and ny_s == ey:
                return dists[nx_s][ny_s]
            queue.append((nx_s, ny_s))
    return -1


print(bfs())