"""
1194 달이 차오른다, 가자.
"""
import sys
from collections import deque

input = sys.stdin.readline
dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def bfs(x, y):
    q = deque()
    q.append((x, y, 0, 0))
    visited = [[[False] * (1 << 6) for _ in range(m)] for _ in range(n)]
    visited[x][y][0] = True

    while q:
        x, y, cnt, key = q.popleft()
        if board[x][y] == '1':
            return cnt
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny][key]:
                    if board[nx][ny] == '1' or board[nx][ny] == '.':
                        visited[nx][ny][key] = True
                        q.append((nx, ny, cnt + 1, key))
                    elif 'a' <= board[nx][ny] <= 'f':
                        temp = key | (1 << (ord(board[nx][ny]) - ord('a')))
                        visited[nx][ny][temp] = True
                        q.append((nx, ny, cnt + 1, temp))
                    elif 'A' <= board[nx][ny] <= 'F':
                        temp = key & (1 << (ord(board[nx][ny]) - ord('A')))
                        if temp:
                            visited[nx][ny][key] = True
                            q.append((nx, ny, cnt + 1, key))
    return -1


n, m = map(int, input().split())
board = [list(input().strip()) for _ in range(n)]
for i in range(n):
    for j in range(m):
        if board[i][j] == '0':
            start_x, start_y = i, j
            board[i][j] = '.'

print(bfs(start_x, start_y))
