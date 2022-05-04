"""
1952 달팽이 2

"""
import sys
input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
n, m = map(int, input().split())
graph = [[False] * m for _ in range(n)]
graph[0][0] = 1
x, y = 0, 0
idx = 0
cnt = 0
while True:
    if idx == 4:
        idx = 0
    nx, ny = x + dx[idx], y + dy[idx]
    if nx < 0 or nx >= n or ny < 0 or ny >= m:
        cnt += 1
        idx += 1
        continue
    if graph[nx][ny] != 0:
        cnt += 1
        idx += 1
        continue
    graph[nx][ny] = graph[x][y] + 1
    x, y = nx, ny
    if graph[nx][ny] == n * m:
        break

print(cnt)
# for i in graph:
#     print(i)
