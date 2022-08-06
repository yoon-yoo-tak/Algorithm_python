"""

"""
from collections import deque
from sys import stdin
input = stdin.readline

ex, ey, ans = 0, 0, 0
dx, dy = (0, -1, 0, 1), (-1, 0, 1, 0)
r, c = map(int, input().split())
lake = [list(input().strip()) for _ in range(r)]
water_visited = [[False]*c for _ in range(r)]
swan_visited = [[False]*c for _ in range(r)]
water_q, temp_water_q = deque(), deque()
swan_q, temp_swan_q = deque(), deque()

def bfs():
    while water_q:
        x, y = water_q.popleft()
        lake[x][y] = '.'
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if nx < 0 or nx >= r or ny < 0 or ny >= c:
                continue
            if water_visited[nx][ny]:
                continue
            if lake[nx][ny] == '.':
                water_q.append((nx, ny))
            else:
                temp_water_q.append((nx, ny))
            water_visited[nx][ny] = True

def can_go():
    while swan_q:
        x, y = swan_q.popleft()
        if x == ex and y == ey:
            return True
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if nx < 0 or nx >= r or ny < 0 or ny >= c:
                continue
            if swan_visited[nx][ny]:
                continue
            if lake[nx][ny] == '.':
                swan_q.append((nx, ny))
            else:
                temp_swan_q.append((nx, ny))
            swan_visited[nx][ny] = True
    return False

for i in range(r):
    for j in range(c):
        if lake[i][j] == 'L':
            if not swan_q:
                swan_q.append((i, j))
                swan_visited[i][j] = True
            else:
                ex, ey = i, j
            lake[i][j] = '.'
        if lake[i][j] == '.':
            water_q.append((i, j))
            water_visited[i][j] = True
while True:
    bfs()
    if can_go():
        break
    water_q, temp_water_q = temp_water_q, deque()
    swan_q, temp_swan_q = temp_swan_q, deque()
    ans += 1
print(ans)
