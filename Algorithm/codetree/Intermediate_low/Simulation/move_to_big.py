"""
숫자가 더 큰 인접한 곳으로 이동
"""
import sys

input = sys.stdin.readline

n, r, c = map(int, input().split())
r -= 1
c -= 1
board = [list(map(int, input().split())) for _ in range(n)]
dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def simulate(x, y):
    tempx, tempy = x, y
    for dx, dy in dxy:
        nx, ny = x + dx, y + dy
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        if board[nx][ny] > board[tempx][tempy]:
            return nx, ny
    return -1

ans = []
ans.append(board[r][c])
while True:
    if simulate(r, c) == -1:
        break
    r, c = simulate(r, c)
    ans.append(board[r][c])

print(*ans)


