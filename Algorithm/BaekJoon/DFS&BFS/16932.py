"""
16932 모양 만들기
"""
import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y):
    cnt = 1
    q.append((x, y))
    visited[x][y] = True
    while q:
        x, y = q.popleft()
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if visited[nx][ny]:
                continue
            if board[nx][ny] == 0:
                continue
            q.append((nx, ny))
            visited[nx][ny] = True
            cnt += 1
    return cnt

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]
ans = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            board[i][j] = 1
            q = deque()
            visited = [[False] * m for _ in range(n)]
            for k in range(n):
                for l in range(m):
                    if board[k][l] == 1:
                        ans = max(ans, bfs(k, l))
            board[i][j] = 0
print(ans)