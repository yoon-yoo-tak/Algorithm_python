import sys

input = sys.stdin.readline

n = int(input())
order = []
for i in range(n):
    a, b = input().split()
    order.append((a, int(b)))
dir = ['N', 'W', 'S', 'E']
dy = [1, 0, -1, 0]
dx = [0, -1, 0, 1]
ans = 0
cnt = 0
flag = False
x, y = 0, 0
for direction, time in order:
    for i in range(time):
        cnt += 1
        nx, ny = x + dx[dir.index(direction)], y + dy[dir.index(direction)]
        if nx == 0 and ny == 0:
            ans = cnt
            flag = True
            break
        x, y = nx, ny
    if flag:
        break

print(ans if ans != 0 else -1)