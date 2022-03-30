"""

16173, 16174 점프왕 쩰리(Small), 점프왕 쩰리(large) 둘 다 가능

"""
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
dxy = [(0, 1), (1, 0)]
visit = [[False] * n for _ in range(n)]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visit[x][y] = True
    while q:
        x, y = q.popleft()
        if a[x][y] == -1:
            return 'HaruHaru'
        for dx, dy in dxy:
            nx = x + dx * a[x][y]
            ny = y + dy * a[x][y]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if visit[nx][ny]:
                continue
            q.append((nx, ny))
            visit[nx][ny] = True
    return 'Hing'

print(bfs(0, 0))