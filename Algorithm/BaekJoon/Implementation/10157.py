"""
10157 자리배정

"""

import sys

input = sys.stdin.readline
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
idx = 0
y, x = map(int, input().split())
ls = [[0] * y for _ in range(x)]
px, py = x - 1, 0
ls[px][py] = 1
while True:
    if idx == 4:
        idx = 0
    nx, ny = px + dx[idx], py + dy[idx]
    if nx < 0 or ny < 0 or nx >= x or ny >= y:  # 범위를 벗어나면 > 방향을 바꿔준다.
        idx += 1
        continue
    if ls[nx][ny] != 0:  # 쭉 채우다가 0이 아닌 값이면 방향을 바꿔준다.
        idx += 1
        continue
    ls[nx][ny] = ls[px][py] + 1
    px, py = nx, ny
    if ls[nx][ny] == x * y:
        break
k = int(input())
if k > x * y:
    print(0)
else:
    for i in range(x):
        for j in range(y):
            if ls[i][j] == k:
                print(j + 1, abs(x - i))
                sys.exit()
