"""

1926 그림

"""
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

a = [list(map(int, input().split())) for _ in range(n)]
visit = [[False] * m for _ in range(n)]

dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def bfs(x, y):
    q = deque()
    count = 0
    q.append((x, y))
    visit[x][y] = True
    while q:
        x, y = q.popleft()
        count += 1
        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if visit[nx][ny]:
                continue
            if a[nx][ny] != 1:
                continue
            q.append((nx, ny))
            visit[nx][ny] = True
    return count


c_ls = []
total = 0
for i in range(n):
    for j in range(m):
        if a[i][j] == 1 and not visit[i][j]:
            c_ls.append(bfs(i, j))
            total += 1

print(total)
if len(c_ls) == 0:
    print(0)
else:
    print(max(c_ls))