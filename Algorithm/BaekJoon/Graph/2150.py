"""
2150 Strongly Connected Component
"""
import sys
from collections import defaultdict
sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

def forward_dfs(x):
    visited.add(x)
    for next in forward_g[x]:
        if next not in visited:
            forward_dfs(next)
    stack.append(x)

def reverse_dfs(x, scc):
    visited.add(x)
    scc.append(x)
    for next in reverse_g[x]:
        if next not in visited:
            scc = reverse_dfs(next, scc)
    return scc

def kosaraju():
    global visited
    answer = []
    for i in range(1, v + 1):
        if i not in visited:
            forward_dfs(i)
    visited = set() # 초기화
    while stack:
        scc = []
        x = stack.pop()
        if x in visited:
            continue
        answer.append(sorted(reverse_dfs(x, scc)))
    return answer


v, e = map(int, input().split())
forward_g = defaultdict(list)
reverse_g = defaultdict(list)
for _ in range(e):
    a, b = map(int, input().split())
    forward_g[a].append(b)
    reverse_g[b].append(a)

stack = []
visited = set()
answer = kosaraju()
print(len(answer))
for i in sorted(answer):
    print(*i,end=' -1\n')

# """
# 타-잔
# """
# v, e = map(int, input().split())
# graph = [[] for _ in range(v + 1)]
# for _ in range(e):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#
# stack = []
# low = [-1] * (v + 1)
# ids = [-1] * (v + 1)
# visited = [0] * (v + 1)
# idid = 0
# result = []
#
# def dfs(x, low, ids, visited, stack):
#     global idid
#     ids[x] = idid
#     low[x] = idid
#     idid += 1
#     visited[x] = 1
#     stack.append(x)
#     for ne in graph[x]:
#         if ids[ne] == -1:
#             dfs(ne, low, ids, visited, stack)
#             low[x] = min(low[x], low[ne])
#         elif visited[ne] == 1:
#             low[x] = min(low[x], ids[ne])
#     w = -1
#     scc = []
#     if low[x] == ids[x]:
#         while w != x:
#             w = stack.pop()
#             scc.append(w)
#             visited[w] = -1
#         result.append(sorted(scc))
#
# for i in range(1, v + 1):
#     if ids[i] == -1:
#         dfs(i, low, ids, visited, stack)
# print(len(result))
# for i in sorted(result):
#     print(*i, -1)
