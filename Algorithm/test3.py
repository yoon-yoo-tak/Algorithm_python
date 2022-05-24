import sys
from collections import deque
input = sys.stdin.readline


m, n = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(n)]
dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]
ans = 0
q = deque()
for i in range(n):
	for j in range(m):
		if tomato[i][j] == 1:
			q.append((i, j))

while q:
	x, y = q.popleft()
	for dx, dy in dxy:
		nx, ny = x + dx, y + dy
		if 0 <= nx < n and 0 <= ny < m and tomato[nx][ny] == 0:
			tomato[nx][ny] = tomato[x][y] + 1
			q.append((nx, ny))

for i in tomato:
	for j in i:
		if j == 0:
			print(-1)
			sys.exit()
	ans = max(ans, max(i))
print(ans - 1)