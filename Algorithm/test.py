import sys
input = sys.stdin.readline
n, m = map(int, input().split())
ls = [list(input().strip()) for _ in range(n)]
ls1 = [[-1] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if ls[i][j] == 'c':
            ls1[i][j] = 0
for i in range(n):
    for j in range(m - 1):
        if ls1[i][j] >= 0 and ls1[i][j + 1] == -1:
            ls1[i][j + 1] = ls1[i][j] + 1
for i in ls1:
    print(*i)


