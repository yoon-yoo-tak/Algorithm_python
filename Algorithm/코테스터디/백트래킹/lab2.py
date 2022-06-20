"""
연구소 2
"""
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(n)]
dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]
virus_pos = []
for i in range(n):
    for j in range(n):
        if lab[i][j] == 2:
            virus_pos.append((i, j))
            lab[i][j] = 0

def bfs():
    q = deque()
    dist = [[-1] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if lab[i][j] == 2:
                q.append((i, j))
                dist[i][j] = 0
    while q:
        x, y = q.popleft()
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if dist[nx][ny] != -1:
                continue
            if lab[nx][ny] != 0:
                continue
            q.append((nx, ny))
            dist[nx][ny] = dist[x][y] + 1
    max_time = 0
    for i in range(n):
        for j in range(n):
            if lab[i][j] == 0 and dist[i][j] == -1:  # 빈 공간인데 -1이다 ?  >> 바이러스가 도달하지 못했다.
                return 987654321
            max_time = max(max_time, dist[i][j])

    return max_time


ans = 987654321


def rec(k, cnt):
    global ans
    if cnt == m:
        ans = min(ans, bfs())
        return
    if k == len(virus_pos):
        return
    else:
        lab[virus_pos[k][0]][virus_pos[k][1]] = 2
        rec(k + 1, cnt + 1)
        lab[virus_pos[k][0]][virus_pos[k][1]] = 0
        rec(k + 1, cnt)

rec(0, 0)

print(ans if ans != 987654321 else -1)

