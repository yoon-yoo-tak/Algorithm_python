"""
16954 움직이는 미로 탈출
"""
import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y, time):
    q = deque()
    q.append((x, y, time))
    while q:
        x, y, now = q.popleft()
        for i in range(9):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= 8 or ny < 0 or ny >= 8:
                continue
            if board[nx - now][ny] == '#':
                continue
            if board[nx - now - 1][ny] == '#':
                continue
            if nx - now < 0:
                return 1
            q.append((nx, ny, now + 1))
    return 0


board = [list(input().strip()) for _ in range(8)]
dx = [0, 0, 0, -1, 1, -1, 1, 1, -1]
dy = [0, -1, 1, 0, 0, -1, -1, 1, 1]
print(bfs(7, 0, 0))