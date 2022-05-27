import sys
from collections import deque
input = sys.stdin.readline


def bfs():
    global gram
    q = deque()
    q.append((0, 0))
    dist[0][0] = 0
    while q:
        x, y = q.popleft()
        if castle[x][y] == 2:  # 현재 위치에 칼이 있으면
            gram = N - 1 - x + M - 1 - y + dist[x][y]  # 공주까지의 최단거리로 갱신
        if x == N - 1 and y == M - 1:  # 현재 위치가 공주 위치라면
            return min(dist[x][y], gram)  # 칼이 있을 때의 최단거리와 없을 때의 최단거리와 비교하여 return
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= N or ny < 0 or ny >= M:  # 범위 체크
                continue
            if castle[nx][ny] == 1:  # 벽인지 체크
                continue
            if dist[nx][ny] != -1:  # 방문한 곳인지 체크
                continue
            q.append((nx, ny))
            dist[nx][ny] = dist[x][y] + 1
    return gram

N, M, T = map(int, input().split())
castle = [list(map(int, input().split())) for _ in range(N)]
dist = [[-1] * M for _ in range(N)]
dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]
gram = 9876543210

ans = bfs()

print('Fail' if ans > T else ans)