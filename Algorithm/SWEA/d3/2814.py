"""
2814 최장 경로
"""


def dfs(v, cnt):
    global max_cnt

    max_cnt = max(max_cnt, cnt)

    for w in range(1, N + 1):
        if graph[v][w] and not visited[w]:
            visited[w] = 1
            dfs(w, cnt + 1)
            visited[w] = 0


T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())
    graph = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

    for _ in range(M):
        x, y = map(int, input().split())
        graph[x][y] = 1
        graph[y][x] = 1

    max_cnt = 1
    for i in range(1, N + 1):
        visited = [0 for _ in range(N + 1)]
        visited[i] = 1
        dfs(i, 1)

    print('#{} {}'.format(t, max_cnt))