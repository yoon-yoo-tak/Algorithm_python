"""
이코테 구현파트 연습문제 - 게임 개발

1. 현재 위치에서 현재 방향을 기준으로 왼쪽방향( 반시계 방향으로 90도 회전) 부터 차례대로 갈 곳을 정한다.
2. 캐릭터의 바로 왼쪽 방향에 아직 가보지 않은 칸이 존재한다면, 왼쪽 방향으로 회전한 다음 왼쪽으로 한 칸 전진한다. 왼쪽 방향에 가보지 않은 칸이 없다면, 왼쪽 방향으로 회전만  수행하고
   1단계로 돌아간다.
3. 만약 네 방향 모두 이미 가본 칸이거나 바다로 되어 있는 경우에는, 바라보는 방향을 유지한 채로 한 칸 뒤로 가고 1단계로 돌아간다.
   단, 이때 뒤쪽 방향이 바다인 칸이라 뒤로 갈 수 없는 경우에는 움직임을 멈춘다.
"""

import sys

input = sys.stdin.readline

n, m = map(int, input().split())

d = [[0] * m for _ in range(n)]
x, y, direction = map(int, input().split())
d[x][y] = 1

arr = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

count = 1
turn_time = 0

while True:
    turn_left()
    nx, ny = x + dx[direction], y + dy[direction]

    if d[nx][ny] == 0 and arr[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1

    if turn_time == 4:
        nx, ny  = x - dx[direction], y - dy[direction]

        if arr[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0

print(count)
