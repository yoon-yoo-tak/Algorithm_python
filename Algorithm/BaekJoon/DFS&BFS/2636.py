"""
2636 치즈
"""

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]
cz = []
def bfs():
    q = deque()
    visit = [[False] * m for _ in range(n)]
    q.append([0,0])
    visit[0][0] = True
    cnt = 0
    while q:
        x, y = q.popleft()
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and not visit[nx][ny]:
                if graph[nx][ny] == 0:
                    visit[nx][ny] = True
                    q.append((nx, ny))
                elif graph[nx][ny] == 1:
                    graph[nx][ny] = 0
                    cnt += 1
                    visit[nx][ny] = True
    cz.append(cnt)
    return cnt

time = 0
while True:
    time += 1
    cnt = bfs()
    for i in graph:
        print(*i)
    print()
    if cnt == 0:
        break
print(time - 1)
print(cz[-2])