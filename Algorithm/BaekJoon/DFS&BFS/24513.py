"""
24513 좀비 바이러스

1. 아이디어
2. 시간복잡도
3. 자료구조
"""

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
village = []
visit = [[0] * m for _ in range(n)]
dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]

q = deque()

for i in range(n):
    vill = list(map(int, input().split()))
    for j in range(m):
        if vill[j] == 1:
            q.append((i, j, 1, 0))
        elif vill[j] == 2:
            q.append((i, j, 2, 0))
    village.append(vill)

while q:
    x, y, num, dist = q.popleft()
    if village[x][y] != 3:
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if village[nx][ny] == 0:
                    village[nx][ny] = num
                    visit[nx][ny] = dist + 1
                    q.append((nx, ny, num, dist + 1))
                elif village[nx][ny] != -1 and village[nx][ny] != num:
                    if visit[nx][ny] == dist + 1:
                        village[nx][ny] = 3

one, two, three = 0, 0, 0

for i in village:
    one += i.count(1)
    two += i.count(2)
    three += i.count(3)
print(one, two, three)
