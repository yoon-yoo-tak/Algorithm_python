"""
20165 인내의 도미노 장인 호석
"""
import sys

input = sys.stdin.readline

n, m, r = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
check = [[True] * m for _ in range(n)]
dxy = {
    'N': (-1, 0),
    'S': (1, 0),
    'E': (0, 1),
    'W': (0, -1)
}

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def attack(x, y, direction):
    global score
    if not check[x][y]:
        return
    dx, dy = dxy[direction]
    cnt = board[x][y]
    while in_range(x, y) and cnt >= 1:
        if check[x][y]:
            score += 1
            cnt = max(cnt - 1, board[x][y] - 1)
        else:
            cnt -= 1
        check[x][y] = False
        x += dx
        y += dy




score = 0
for _ in range(r):
    a_x, a_y, dir = input().split()
    a_x = int(a_x) - 1
    a_y = int(a_y) - 1
    d_x, d_y = map(lambda x: x - 1, map(int, input().split()))
    attack(a_x, a_y, dir)
    check[d_x][d_y] = True

print(score)
for i in range(n):
    for j in range(m):
        print('S' if check[i][j] else 'F', end=' ')
    print()

