"""
연구소
0 가능
1 벽
2 바이러스
"""
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(n)]
zero_pos = [[i, j] for i in range(n) for j in range(m) if lab[i][j] == 0]
dxy = [[1, 0], [0, 1], [-1, 0], [0, -1]]
ans = 0
def bfs():
    global ans
    q = deque()
    visited = [[False] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if lab[i][j] == 2:
                q.append((i, j))
                visited[i][j] = True
    while q:
        x, y = q.popleft()
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if visited[nx][ny]:
                continue
            if lab[nx][ny]:
                continue
            q.append((nx, ny))
            visited[nx][ny] = True
    cnt = 0
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and lab[i][j] == 0:
                cnt += 1
    ans = max(ans, cnt)


def rec(k, cnt):
    if cnt == 3: # 3 개를 뽑았다
        bfs()
        return
    if k == len(zero_pos):  # 끝까지 가봤으면 끝
        return
    else:
        lab[zero_pos[k][0]][zero_pos[k][1]] = 1  # 벽으로
        rec(k + 1, cnt + 1)  # 현재값저장하고 다음위치 보러가기
        lab[zero_pos[k][0]][zero_pos[k][1]] = 0  # 벽으로
        rec(k + 1, cnt)  # 현재값 안보고 다음위치 보러가기


rec(0, 0)

print(ans)
