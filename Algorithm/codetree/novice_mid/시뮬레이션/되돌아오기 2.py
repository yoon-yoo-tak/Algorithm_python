import sys

input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
dir, x, y = 0, 0, 0
s = input().strip()
ans = -1
for i in range(len(s)):
    if s[i] == 'F':
        nx, ny = x + dx[dir], y + dy[dir]
        if nx == 0 and ny == 0:
            ans = i + 1
            break
        x, y = nx, ny
    elif s[i] == 'R':
        dir = (dir + 1) % 4
    else:
        dir = (dir - 1) % 4

print(ans)