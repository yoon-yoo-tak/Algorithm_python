"""
11725 트리의 부모 찾기

"""
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100005)


n = int(input())
graph = [[] for _ in range(n + 1)]
visit = [False] * (n + 1)
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

parent = [0] * (n + 1)
#
# def dfs(v):
#     visit[v] = True
#     for i in graph[v]:
#         if not visit[i]:
#             parent[i] = v
#             dfs(i)
#             visit[i] = True

# dfs(1)
# for i in parent[2:]:
#     print(i)

def dfs1(x, par):
    for y in graph[x]:
        if y == par:
            continue
        parent[y] = x
        dfs1(y, x)

dfs1(1, -1)
for i in parent[2:]:
    print(i)