"""

18352 특정 거리의 도시 찾기

"""
import sys
from collections import deque
input = sys.stdin.readline

n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n + 1)]
dist = [-1] * (n + 1)
ans = []

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

def bfs(v):
    q = deque()
    q.append(v)
    dist[v] = 0
    while q:
        n = q.popleft()
        for i in graph[n]:
            if dist[i] != -1:
                continue
            q.append(i)
            dist[i] = dist[n] + 1
            ans.append([i, dist[i]])
bfs(x)
res = []
for i in ans:
    if i[1] == k:
        res.append(i[0])

if len(res) == 0:
    print(-1)
else:
    res.sort()
    for i in res:
        print(i)