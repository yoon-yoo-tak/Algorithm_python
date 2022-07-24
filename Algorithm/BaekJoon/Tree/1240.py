"""
1240 노드사이의 거리
- rooted tree로 바꿔서 dfs로 거리계산하기
"""
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    x, y, c = map(int, input().split())
    graph[x].append((y, c))
    graph[y].append((x, c))

def dfs(x, prev, target, dist):
    if x == target:
        print(dist)
        return
    for y, c in graph[x]:
        if y == prev:
            continue
        dfs(y, x, target, dist + c)
for _ in range(m):
    x, y = map(int, input().split())
    dfs(x, -1, y, 0)