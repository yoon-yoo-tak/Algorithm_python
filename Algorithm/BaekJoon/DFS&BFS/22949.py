"""
22949 회전 미로 탐색
"""
import sys
from collections import deque
input = sys.stdin.readline


def get_area(x, y, k):
    x, y = x // 4 * 4, y // 4 * 4
    return x * k + y


def next_pos(x, y):
    nx, ny = x // 4 * 4, y // 4 * 4
    x %= 4
    y %= 4
    return y + ny, 3 - x + nx

k = int(input())
n = k * 4
board = [list(input().strip()) for _ in range(n)]
board_copy = [[['.'] * n for _ in range(n)] for _ in range(4)]
dist = [[[-1] * n for _ in range(n)] for _ in range(4)]
dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]

for i in range(n):
    for j in range(n):
        if board[i][j] == 'S':
            start_x, start_y = i, j
            board[i][j] = '.'
        if board[i][j] == 'E':
            end_x, end_y = i, j
            board[i][j] = '.'
for i in range(k):
    for j in range(k):
        x, y = 4 * i, 4 * j
        temp = []
        for p in range(4):
            temp.append(board[x + p][y:y + 4])
        for p in range(4):
            for q in range(4):
                for r in range(4):
                    board_copy[p][x + q][y + r] = temp[q][r]
            temp = [list(l) for l in list(zip(*temp[::-1]))]

q = deque()
q.append((0, start_x, start_y))
dist[0][start_x][start_y] = 0
while q:
    cnt, x, y = q.popleft()
    area_now = get_area(x, y, k)
    for dx, dy in dxy:
        nx, ny = x + dx, y + dy
        area_next = get_area(nx, ny, k)
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        if area_next == area_now:
            if board_copy[cnt][nx][ny] == '#':
                continue
            nx, ny = next_pos(nx, ny)  # 90도 회전
            n_cnt = (cnt + 1) % 4
            if dist[n_cnt][nx][ny] != -1:
                continue
            dist[n_cnt][nx][ny] = dist[cnt][x][y] + 1
            q.append((n_cnt, nx, ny))
        else:
            if board_copy[0][nx][ny] == '#':
                continue
            nx, ny = next_pos(nx, ny)
            if dist[1][nx][ny] != -1:
                continue
            dist[1][nx][ny] = dist[cnt][x][y] + 1
            q.append((1, nx, ny))
    n_cnt, nx, ny = (cnt + 1) % 4, x, y
    nx, ny = next_pos(nx, ny)
    if dist[n_cnt][nx][ny] == -1:
        dist[n_cnt][nx][ny] = dist[cnt][x][y] + 1
        q.append((n_cnt, nx, ny))


ans = -1
for i in range(4):
    dd = dist[i][end_x][end_y]
    end_x, end_y = next_pos(end_x, end_y)
    if dd == -1:
        continue
    if ans == -1:
        ans = dd
    else:
        ans = min(ans, dd)

print(ans)


