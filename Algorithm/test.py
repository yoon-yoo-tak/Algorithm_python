import sys
from collections import deque
input = sys.stdin.readline

n, m, v = map(int, input().split())

graph = [[] for _ in range(n + 1)]
visit = [False] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()

def dfs(v):
    visit[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visit[i]:
            dfs(i)
            visit[i] = True

def bfs(v):
    q = deque([v])
    visit[v] = True
    while q:
        n = q.popleft()
        print(n, end = ' ')
        for i in graph[n]:
            if not visit[i]:
                q.append(i)
                visit[i] = True

dfs(v)
print()
visit = [False] * (n + 1)
bfs(v)