"""
16933 벽 부수고 이동하기 3
"""
import sys
from collections import deque
input = sys.stdin.readline


def in_range(x, y, z):
    return 0 <= x < n and 0 <= y < m and not visited[x][y][z]


def bfs(x, y, cnt):
    q = deque()
    q.append((x, y, cnt))
    is_day = 1
    while q:
        is_night = False if is_day > 0 else True
        for _ in range(len(q)):
            x, y, cnt = q.popleft()
            now = abs(is_day)
            if x == n - 1 and y == m - 1:
                return now
            for dx, dy in dxy:
                nx, ny = x + dx, y + dy
                if in_range(nx, ny, cnt):
                    if not board[nx][ny]:
                        visited[nx][ny][cnt] = now + 1
                        q.append((nx, ny, cnt))
                    elif cnt < k and not in_range(nx, ny, cnt + 1):
                        if not is_night:
                            visited[nx][ny][cnt + 1] = now + 1
                            q.append((nx, ny, cnt + 1))
                        else:
                            q.append((x, y, cnt))
        is_day = is_day + 1 if is_day > 0 else is_day - 1
        is_day *= -1
    return -1



n, m, k = map(int, input().split())
board = [list((map(int, input().strip()))) for _ in range(n)]
dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]
visited = [[[0] * (k + 1) for _ in range(m)] for _ in range(n)]
visited[0][0] = [1] * (k + 1)
print(bfs(0, 0, 0))