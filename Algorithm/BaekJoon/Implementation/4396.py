"""
4396 지뢰 찾기

"""
import sys
input = sys.stdin.readline
n = int(input())
board = [list(input().strip()) for _ in range(n)]
opened = [list(input().strip()) for _ in range(n)]

mine_pos = [(i, j) for i in range(n) for j in range(n) if board[i][j] == '*']
dxy = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]

for i in range(n):
    for j in range(n):
        if opened[i][j] == 'x':
            if board[i][j] == '.':
                opened[i][j] = 0
                for dx, dy in dxy:
                    nx = i + dx
                    ny = j + dy
                    if nx < 0 or nx >= n or ny < 0 or ny >= n:
                        continue
                    if board[nx][ny] == '*':
                        opened[i][j] += 1
            else:
                for x, y in mine_pos:
                    opened[x][y] = '*'

for i in range(n):
    for j in range(n):
        opened[i][j] = str(opened[i][j])

for i in opened:
    print(''.join(i))

