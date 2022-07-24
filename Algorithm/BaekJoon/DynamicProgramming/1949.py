"""
1949 우수 마을
"""
import sys
sys.setrecursionlimit(int(1e9))
input = sys.stdin.readline


def dfs(x, parent):
    dp[x][1] = a[x]
    for y in graph[x]:
        if y == parent:
            continue
        dfs(y, x)
        dp[x][0] += max(dp[y])
        dp[x][1] += dp[y][0]


n = int(input())
a = [0] + list(map(int, input().split()))
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

dp = [[0] * 2 for _ in range(n + 1)]

dfs(1, -1)
print(max(dp[1]))