"""
3190 뱀
"""

import sys
from collections import deque
input = sys.stdin.readline


def turn(d, c):
    if c == 'L':
        d = (d - 1) % 4
    else:
        d = (d + 1) % 4
    return d


def snake():
    x, y = 1, 1
    data[x][y] = 2
    d = 0
    time = 0
    idx = 0
    q = deque()
    q.append((x, y))
    while True:
        nx, ny = x + dx[d], y + dy[d]
        if 1 <= nx <= n and 1 <= ny <= n and data[nx][ny] != 2:
            if data[nx][ny] == 0:
                data[nx][ny] = 2
                q.append((nx, ny))
                px, py = q.popleft()
                data[px][py] = 0
            if data[nx][ny] == 1:
                data[nx][ny] = 2
                q.append((nx, ny))
        else:
            time += 1
            break
        x, y = nx, ny
        time += 1
        if idx < l and time == info[idx][0]:
            d = turn(d, info[idx][1])
            idx += 1
    return time



n = int(input())
k = int(input())
data = [[0] * (n + 1) for _ in range(n + 1)]
info = []

for _ in range(k):
    a, b = map(int, input().split())
    data[a][b] = 1

l = int(input())

for _ in range(l):
    a, b = input().split()
    info.append((int(a), b))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

print(snake())