"""
14503 로봇 청소기
"""

import sys

input = sys.stdin.readline
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left(dir):
    dir = (dir - 1) % 4
    return dir

def check_left(x, y, dir):  # 바로왼쪽방향 확인
    dir = turn_left(dir)
    if graph[x + dx[dir]][y + dy[dir]] == 0:
        return True
    return False

def go_forward(x, y, dir):  # 바라보는 방향으로 전진
    x, y = x + dx[dir], y + dy[dir]
    return x, y

def go_backward(x, y, dir):  # 뒤로 후진
    dir ^= 2
    x, y = x + dx[dir], y + dy[dir]
    return x, y

def clean(x, y):  # 현재위치 청소
    graph[x][y] = 2

def check_every(x, y, dir): # 주변 모두 청소되어있는지
    for _ in range(4):
        if check_left(x, y, dir):
            return False
        dir = turn_left(dir)
    return True

n, m = map(int, input().split())
r, c, d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
flag = False

while True:
    clean(r, c)
    if check_left(r, c, d):  # 왼쪽칸이 청소되어있지 않는 빈공간이라면
        d = turn_left(d)
        r, c = go_forward(r, c, d)
        continue
    else:  # 왼쪽칸이 청소되어있거나 벽이면
        if check_every(r, c, d):  # 4방이 청소되어있으면
            temp_x, temp_y = go_backward(r, c, d)
            if graph[temp_x][temp_y] == 1:
                break
            else:
                r, c = temp_x, temp_y
                continue
        else:  # 청소할 곳이 있으면
            while not check_left(r, c, d):  # 청소할곳 찾을때까지 회전
                d = turn_left(d)
            continue

ans = 0
for i in graph:
    ans += i.count(2)
print(ans)