import sys

input = sys.stdin.readline

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]
idx, x, y = 0, 0, 0
s = input().strip()
for i in s:
    if i == 'F':
        x, y = x + dx[idx], y + dy[idx]
    elif i == 'L':
        idx = (idx - 1) % 4
    else:
        idx = (idx + 1) % 4
print(x, y)