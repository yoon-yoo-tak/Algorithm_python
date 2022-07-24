"""
3977 축구 전술
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


def reverse_dfs(x, visited, stack):
    visited.add(x)
    ids[x] = idx
    stack.append(x)
    for next in reverse_g[x]:
        if next not in visited:
            reverse_dfs(next, visited, stack)

tt = int(input())
for t in range(tt):
    if t in range(1, tt):
        input()
    n, move = map(int, input().split())
    forward_g = defaultdict(list)
    reverse_g = defaultdict(list)
    for _ in range(move):
        a, b = map(int, input().split())
        forward_g[a].append(b)
        reverse_g[b].append(a)
    stack = []
    visited = set()

    for i in range(n):
        if i not in visited:
            forward_dfs(i, visited, stack)

    result = [[] for _ in range(n)]
    visited = set()
    idx = -1
    ids = [-1] * n
    while stack:
        scc = []
        x = stack.pop()
        if x not in visited:
            idx += 1
            reverse_dfs(x, visited, scc)
            result[idx] = scc
    scc_indegree = [0] * (idx + 1)

    for i in range(n):
        for j in forward_g[i]:
            if ids[i] != ids[j]:
                scc_indegree[ids[j]] += 1
    cnt = 0
    temp = []
    for i in range(idx + 1):
        if scc_indegree[i] == 0:
            for j in result[i]:
                temp.append(j)
            cnt += 1
    if cnt == 1:
        for i in sorted(temp):
            print(i)
    else:
        print('Confused')


