import sys

input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

def find(x, y, x1, y1):
    temp = 0
    for i in range(x, x1 + 1):
        for j in range(y, y1 + 1):
            if board[i][j] <= 0:
                return 0
            val = (x1 - x + 1) * (y1 - y + 1)
            temp = max(temp, val)
    return temp

ans = -1

for i in range(n):
    for j in range(m):
        for k in range(i, n):
            for l in range(j, m):
                find(i, j, k, l)
                ans = max(ans, find(i, j, k, l))
print(ans if ans > 0 else -1)

