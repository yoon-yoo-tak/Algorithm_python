"""
15900 나무 탈출 (재귀)
"""
import sys
sys.setrecursionlimit(500005)
input = sys.stdin.readline
def dfs(x, prev, depth):
    global total_leaf
    if x != 1 and len(graph[x]) == 1:
        total_leaf += depth
    for y in graph[x]:
        if y == prev:
            continue
        dfs(y, x, depth + 1)


n = int(input())
total_leaf = 0
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


dfs(1, -1, 0)
print('Yes' if total_leaf % 2 else 'No')