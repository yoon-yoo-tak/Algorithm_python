"""
24463 미로

아이디어
- 최단거리가 아닌것을 어떻게 걸러내야 하는가
- 양쪽 입구에서 각각 bfs 수행 > 각각의 최단거리간의 합은 일정하다는것 이용 > 합이 다르면 @ 표시

"""

import sys
from collections import deque
input = sys.stdin.readline


def bfs1(x, y):
    q = deque()
    q.append((x, y))
    dist1[x][y] = 0
    while q:
        x, y = q.popleft()
        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if dist1[nx][ny] != -1:
                continue
            if graph[nx][ny] != '.':
                continue
            q.append((nx, ny))
            dist1[nx][ny] = dist1[x][y] + 1


def bfs2(x, y):
    q = deque()
    q.append((x, y))
    dist2[x][y] = 0
    while q:
        x, y = q.popleft()
        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if dist2[nx][ny] != -1:
                continue
            if graph[nx][ny] != '.':
                continue
            q.append((nx, ny))
            dist2[nx][ny] = dist2[x][y] + 1


n, m = map(int, input().split())
graph = [input().strip() for _ in range(n)]
dist1 = [[-1] * m for _ in range(n)]
dist2 = [[-1] * m for _ in range(n)]
dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]

hole = []

# 테두리 구멍 체크
for i in range(m):
    if graph[0][i] == '.':
        hole.append((0, i))
    if graph[n - 1][i] == '.':
        hole.append((n - 1, i))
for i in range(n):
    if graph[i][0] == '.':
        hole.append((i, 0))
    if graph[i][m - 1] == '.':
        hole.append((i, m - 1))
start_x, start_y = hole[0][0], hole[0][1]
end_x, end_y = hole[1][0], hole[1][1]


bfs1(start_x, start_y)

bfs2(end_x, end_y)

for i in dist2:
    print(i)

shortCutVal = dist1[start_x][start_y] + dist2[start_x][start_y]
new_graph = [[] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if graph[i][j] == '+':
            new_graph[i].append('+')
        elif dist1[i][j] + dist2[i][j] != shortCutVal:
            new_graph[i].append('@')
        else:
            new_graph[i].append('.')

for i in new_graph:
    print(''.join(i))

