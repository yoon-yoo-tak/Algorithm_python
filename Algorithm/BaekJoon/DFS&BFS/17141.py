"""
17141 연구소 2

"""
import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline

def bfs(ls):
    q = deque()
    dist = [[-1] * n for _ in range(n)]
    for a, b in ls:
        q.append((a, b))
        dist[a][b] = 0
    while q:
        x, y = q.popleft()
        for dx, dy in dxy:
            nx, ny = x + dx , y + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if dist[nx][ny] != -1:
                continue
            if lab[nx][ny] != 0:
                continue
            q.append((nx, ny))
            dist[nx][ny] = dist[x][y] + 1
    # 0이면서 방문이안된곳이 있다 > 지금 경우의 수로 전체를 감염시킬 수 없다.
    ans = 0
    for i in range(n):
        for j in range(n):
            if lab[i][j] == 0 and dist[i][j] == -1:
                return int(1e9)
            ans = max(ans, dist[i][j])
    return ans

n, m = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(n)]
dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]
virus_pos = [(i, j) for j in range(n) for i in range(n) if lab[i][j] == 2]
for x, y in virus_pos:
    lab[x][y] = 0

# 바이러스 놓기
combi = combinations(virus_pos, m)
res = int(1e9)
for i in combi:
    for x, y in list(i):
        lab[x][y] = 2
    res = min(res, bfs(list(i)))
    for x, y in list(i):
        lab[x][y] = 0

print(-1 if res == int(1e9) else res)

