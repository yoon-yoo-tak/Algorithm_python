import sys

input = sys.stdin.readline

n, t = map(int, input().split())
board = [[-1] * n for _ in range(n)]
r, c, d = input().split()
r = int(r) - 1
c = int(c) - 1
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
direction = ['D', 'R', 'U', 'L']
idx = direction.index(d)
for _ in range(t):
    nx, ny = r + dx[idx], c + dy[idx]
    if nx < 0 or nx >= n or ny < 0 or ny >= n:
        idx ^= 2
        continue
    r, c = nx, ny

print(r + 1, c + 1)