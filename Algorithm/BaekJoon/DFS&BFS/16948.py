"""

16948 데스 나이트

"""

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
a, b, c, d = map(int, input().split())
board = [[-1] * n for _ in range(n)]
dxy = [(-2, -1), (-2, 1), (0, -2), (0, 2), (2, -1), (2, 1)]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    board[x][y] = 0
    while q:
        x, y = q.popleft()
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if board[nx][ny] != -1:
                continue
            q.append((nx, ny))
            board[nx][ny] = board[x][y] + 1

bfs(a, b)
print(board[c][d])
