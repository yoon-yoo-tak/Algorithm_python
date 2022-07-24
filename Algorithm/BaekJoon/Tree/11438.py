"""
11438 LCA 2
"""
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

n = int(input())
parent = [[0] * 21 for _ in range(n + 1)]
visited = [False] * (n + 1)
d = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(x, depth):
    visited[x] = True
    d[x] = depth

    for v in graph[x]:
        if visited[v]:
            continue
        parent[v][0] = x
        dfs(v, depth + 1)

def lca(x, y):
    if d[x] > d[y]:
        x, y = y, x
    for i in range(20, -1, -1):
        if d[y] - d[x] >= 2 ** i:
            y = parent[y][i]
    if x == y:
        return x
    for i in range(20, -1, -1):
        if parent[x][i] != parent[y][i]:
            x = parent[x][i]
            y = parent[y][i]
    return parent[x][0]


dfs(1, 0)
for i in range(1, 20):
    for j in range(1, n + 1):
        parent[j][i] = parent[parent[j][i- 1]][i - 1]

for _ in range(int(input())):
    a, b = map(int, input().split())
    print(lca(a, b))