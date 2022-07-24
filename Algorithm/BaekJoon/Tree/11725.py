"""
11725 트리의 부모 찾기

"""
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100005)


n = int(input())
graph = [[] for _ in range(n + 1)]
parent = [0] * (n + 1)
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(x, par):
    for y in graph[x]:
        if y == par:
            continue
        parent[y] = x
        dfs(y, x)

dfs(1, -1)
for i in parent[2:]:
    print(i)