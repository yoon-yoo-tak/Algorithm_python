import sys

input = sys.stdin.readline

def attack_right_down(a ,b):
    dx = [1, -1]
    dy = [1, -1]
    cnt = 0
    x, y = a, b
    while True:
        nx, ny = x + dx[0], y + dy[0]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            break
        cnt += board[nx][ny]
        x, y = nx, ny
    x, y = a, b
    while True:
        nx, ny = x + dx[1], y + dy[1]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            break
        cnt += board[nx][ny]
        x, y = nx, ny
    return cnt



def attack_left_down(a, b):
    dx = [-1, 1]
    dy = [1, -1]
    cnt = 0
    x, y = a, b
    while True:
        nx, ny = x + dx[0], y + dy[0]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            break
        cnt += board[nx][ny]
        x, y = nx, ny
    x, y = a, b
    while True:
        nx, ny = x + dx[1], y + dy[1]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            break
        cnt += board[nx][ny]
        x, y = nx, ny
    return cnt



for _ in range(int(input())):
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    total = 0
    for i in range(n):
        for j in range(m):
            temp = board[i][j]
            temp += attack_left_down(i, j)
            temp += attack_right_down(i, j)
            total = max(temp, total)
    print(total)