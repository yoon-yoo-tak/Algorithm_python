"""
1726 로봇
"""
import sys
from collections import deque
INF = int(1e9)
input = sys.stdin.readline
dx = [0, 0, 0, 1, -1]
dy = [0, 1, -1, 0, 0]

def change_dir_count(before, after):
    if before == after:
        return 0
    elif (before == 1 and after == 2) or (before == 2 and after == 1):
        return 2
    elif (before == 3 and after == 4) or (before == 4 and after == 3):
        return 2
    else:
        return 1

def bfs():
    q = deque()
    q.append((start_x, start_y, start_dir, 0))
    visited = set()
    while q:
        x, y, d, cnt = q.popleft()
        if x == end_x and y == end_y:
            return cnt + change_dir_count(d, end_dir)
        for i in range(1, 4):
            nx, ny = x + dx[d] * i, y + dy[d] * i
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                break
            if board[nx][ny]:
                break
            if (nx, ny, d, cnt + 1) in visited:
                continue
            q.append((nx, ny, d, cnt + 1))
            visited.add((nx, ny, d, cnt + 1))
        for i in range(1, 5):
            if i != d and (x, y, i, cnt + 1) not in visited:
                q.append((x, y, i, cnt + change_dir_count(d, i)))
                visited.add((x, y, i, cnt + change_dir_count(d, i)))



n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
start_x, start_y, start_dir = map(lambda x: x - 1, map(int, input().split()))
end_x, end_y, end_dir = map(lambda x: x - 1, map(int, input().split()))
start_dir, end_dir = start_dir + 1, end_dir + 1
print(bfs())