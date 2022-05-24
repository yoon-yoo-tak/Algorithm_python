"""
소년 점프
"""
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, [*input().strip()])) for _ in range(n)]
dist = [[[-1] * 3 for _ in range(m)] for _ in range(n)]
q = deque()
dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]

for i in range(3):
    a, b = map(int, input().split())
    q.append((a - 1, b - 1, i))
    dist[a - 1][b - 1][i] = 0
while q:
    x, y, z = q.popleft()
    for dx, dy in dxy:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 0 and dist[nx][ny][z] == -1:
            q.append((nx, ny, z))
            dist[nx][ny][z] = dist[x][y][z] + 1
ans = int(1e9)

cnt = 0
for i in range(n):
    for j in range(m):
        if min(dist[i][j]) != -1:
            if ans > max(dist[i][j]):
                ans = max(dist[i][j])
                cnt = 1
            elif max(dist[i][j]) == ans:
                cnt += 1
if ans == int(1e9):
    print(-1)
else:
    print(ans)
    print(cnt)


