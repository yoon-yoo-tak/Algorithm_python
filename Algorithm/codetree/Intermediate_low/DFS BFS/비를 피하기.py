"""
비를 피하기
0 이동가능
1 벽
2 사람
3 목적지
"""
import sys
from collections import deque
input = sys.stdin.readline


def bfs(x, y):
    dist = [[-1] * n for _ in range(n)]
    q = deque()
    q.append((x, y))
    dist[x][y] = 0
    while q:
        x, y = q.popleft()
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if dist[nx][ny] != -1:
                continue
            if board[nx][ny] == 1:
                continue
            q.append((nx, ny))
            dist[nx][ny] = dist[x][y] + 1
    return dist


n, h, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]
ans = [[0] * n for _ in range(n)]
three = []
for i in range(n):
    for j in range(n):
        if board[i][j] == 3:
            three.append([i, j])

for i in range(n):
    for j in range(n):
        if board[i][j] == 2:
            ans[i][j] = -1
            dist = bfs(i, j)
            temp = int(1e9)
            for x, y in three:
                if dist[x][y] != -1:
                    temp = min(temp, dist[x][y])
            ans[i][j] = temp if temp != int(1e9) else -1

for i in ans:
    print(*i)

