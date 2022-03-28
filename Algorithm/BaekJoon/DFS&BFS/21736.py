"""

21736 헌내기는 친구가 필요해

"""
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
a = [input().strip() for _ in range(n)]
visit = [[False] * m for _ in range(n)]
dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visit[x][y] = True
    count = 0
    while q:
        x, y = q.popleft()
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if visit[nx][ny]:
                continue
            if a[nx][ny] == 'X':
                continue
            q.append((nx, ny))
            visit[nx][ny] = True
            if a[nx][ny] == 'P':
                count += 1
    return count

for i in range(n):
    for j in range(m):
        if a[i][j] == 'I':
            x, y = i, j
ans = bfs(x, y)
if ans:
    print(ans)
else:
    print('TT')
