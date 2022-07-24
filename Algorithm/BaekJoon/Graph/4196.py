"""
4196 도미노
"""
import sys
from collections import defaultdict
sys.setrecursionlimit(int(1e9))
input = sys.stdin.readline


def forward_dfs(x, visited, stack):
    visited.add(x)
    for next in forward_g[x]:
        if next not in visited:
            forward_dfs(next, visited, stack)
    stack.append(x)


def reverse_dfs(x, visited, scc):
    global idx
    visited.add(x)
    ids[x] = idx
    scc.append(x)
    for next in reverse_g[x]:
        if next not in visited:
            reverse_dfs(next, visited, scc)



for _ in range(int(input())):
    v, e = map(int, input().split())
    forward_g = defaultdict(list)
    reverse_g = defaultdict(list)
    visited = set()
    stack = []
    for _ in range(e):
        a, b = map(int, input().split())
        forward_g[a].append(b)
        reverse_g[b].append(a)
    for i in range(1, v + 1):
        if i not in visited:
            forward_dfs(i, visited, stack)
    visited = set()
    result = []
    idx = 0
    ids = [-1] * (v + 1)
    while stack:
        scc = []
        x = stack.pop()
        if x not in visited:
            idx += 1
            reverse_dfs(x, visited, scc)
            result.append(sorted(scc))
    scc_indegree = [0] * (idx + 1)
    for i in range(1, v + 1):
        for j in forward_g[i]:
            if ids[i] != ids[j]:
                scc_indegree[ids[j]] += 1
    ans = 0
    for i in range(1, len(scc_indegree)):
        if scc_indegree[i] == 0:
            ans += 1
    print(ans)