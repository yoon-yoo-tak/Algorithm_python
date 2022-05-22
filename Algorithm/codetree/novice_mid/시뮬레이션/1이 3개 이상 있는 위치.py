import sys

input = sys.stdin.readline

def check(x, y):
    num = 0
    for dx, dy in dxy:
        nx, ny = x + dx, y + dy
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        if ls[nx][ny] == 1:
            num += 1
    return True if num >= 3 else False


n = int(input())
ls = [list(map(int, input().split())) for _ in range(n)]
dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]
cnt = 0
for i in range(n):
    for j in range(n):
        if check(i, j):
            cnt += 1
print(cnt)