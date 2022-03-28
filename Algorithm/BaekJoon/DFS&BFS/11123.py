"""

11123 양무리

"""
import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visit[x][y] = True
    while q:
        x, y = q.popleft()
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and a[nx][ny] == '#' and not visit[nx][ny]:
                q.append((nx, ny))
                visit[nx][ny] = True

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    a = [input().strip() for _ in range(n)]
    visit = [[False] * m for _ in range(n)]
    dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    cnt = 0
    for i in range(n):
        for j in range(m):
            if a[i][j] == '#' and not visit[i][j]:
                bfs(i,j)
                cnt += 1
    print(cnt)
