"""
15681 트리와 쿼리
"""
import sys
sys.setrecursionlimit(int(1e9))
input = sys.stdin.readline


def dfs(x, parent):
    global dp
    dp[x] = 1
    for y in graph[x]:
        if y == parent:
            continue
        dfs(y, x)
        dp[x] += dp[y]


n, r, q = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

dp = [0] * (n + 1)

dfs(r, -1)

for _ in range(q):
    print(dp[int(input())])