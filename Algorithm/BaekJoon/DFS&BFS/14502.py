"""

14502 연구소

"""
import sys
from collections import deque
input = sys.stdin.readline


def dfs(idx, cnt):
    if cnt == 3:
        bfs()
        return
    if idx == len(safe):
        return

    a[safe[idx][0]][safe[idx][1]] = 1
    dfs(idx + 1, cnt + 1)

    a[safe[idx][0]][safe[idx][1]] = 0
    dfs(idx + 1, cnt)

def bfs():
    global ans
    zero_cnt = 0
    q = deque()
    visit = [[False] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if a[i][j] == 2:
                q.append((i, j))
                visit[i][j] = True

    while q:
        x, y = q.popleft()
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if visit[nx][ny]:
                continue
            if a[nx][ny] != 0:
                continue
            q.append((nx, ny))
            visit[nx][ny] = True

    for i in range(n):
        for j in range(m):
            if a[i][j] == 0 and not visit[i][j]:  # not visit이다 > 바이러스가 도달하지 못한 곳이다.
                zero_cnt += 1
    ans = max(ans, zero_cnt)

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

safe = [(i, j) for i in range(n) for j in range(m) if a[i][j] == 0]

ans = 0
dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]

dfs(0, 0)
print(ans)