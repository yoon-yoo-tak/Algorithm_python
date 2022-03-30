"""

13903 출근

multisource bfs로 거리 기록하면 될듯

"""
import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    q = deque()
    for i in range(m):
        if a[0][i] == 1:
            q.append((0, i))
            dist[0][i] = 0
    while q:
        x, y = q.popleft()
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and a[nx][ny] == 1 and dist[nx][ny] == -1:
                q.append((nx, ny))
                dist[nx][ny] = dist[x][y] + 1


n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
dist = [[-1] * m for _ in range(n)]
k = int(input())

dxy = []
for _ in range(k):
    x, y = map(int, input().split())
    dxy.append((x, y))

bfs()
ls = []
for i in dist[n - 1]:
    if i != -1:
        ls.append(i)

if len(ls) == 0:
    print(-1)
else:
    print(min(ls))

