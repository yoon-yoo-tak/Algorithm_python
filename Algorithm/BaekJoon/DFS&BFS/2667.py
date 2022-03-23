"""

2667 단지번호 붙이기

"""
import sys
input = sys.stdin.readline

n = int(input())

a = [input().strip() for _ in range(n)]
visit = [[False]*n for _ in range(n)]
cnt = 0
group = []
d = [[1, 0], [0, 1], [-1, 0], [0, -1]]

def dfs(x,y):
    global cnt
    cnt += 1
    visit[x][y] = True
    for dx, dy in d:
        nx, ny = x + dx, y + dy
        if nx < 0 or nx >= n or ny < 0 or ny >= n :
            continue
        if a[nx][ny] == '0':
            continue
        if visit[nx][ny]:
            continue
        dfs(nx, ny)

for i in range(n):
    for j in range(n):
        if a[i][j] == '0' or visit[i][j]:
            continue
        cnt = 0
        dfs(i, j)
        group.append(cnt)

group.sort()
print(len(group))
for i in group:
    print(i)


