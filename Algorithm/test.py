import sys
input = sys.stdin.readline

def dfs(x, y):
    visit[x][y] = True
    for dx, dy in dxy:
        nx, ny = x + dx, y + dy
        if nx < 0 or nx >= n or ny < 0 or ny >=m:
            continue
        if graph[nx][ny] == 0:
            continue
        if visit[nx][ny]:
            continue
        dfs(nx, ny)


for _ in range(int(input())):
    m, n, k = map(int, input().split())
    graph = [[0] * m for _ in range(n)]
    visit = [[False] * m for _ in range(n)]
    dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    for _ in range(k):
        a, b = map(int, input().split())
        graph[b][a] = 1
    count = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1 and not visit[i][j]:
                dfs(i, j)
                count += 1
    print(count)