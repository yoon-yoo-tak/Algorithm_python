import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    q = deque()
    q.append((a, b))
    visited[a][b] = 0
    while q:
        x, y = q.popleft()
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= 5 or ny < 0 or ny >= 5:
                continue
            if board[nx][ny] == -1:
                continue
            if visited[nx][ny] != -1:
                continue
            q.append((nx, ny))
            visited[nx][ny] = visited[x][y] + 1


dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]
board = [list(map(int, input().split())) for _ in range(5)]
visited = [[-1] * 5 for _ in range(5)]
a, b = map(int, input().split())
bfs()
x = [(i, j) for j in range(5) for i in range(5) if board[i][j] == 1]
print(visited[x[0][0]][x[0][1]])



