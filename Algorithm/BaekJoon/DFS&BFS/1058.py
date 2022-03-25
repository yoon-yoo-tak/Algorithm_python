"""

1058 친구

2-친구가 많은 사람? > 모든 노드들에 대해 탐색해서 깊이가 1, 2인 수가 가장 많은 노드가 답이라고 생각

"""
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
a = [input().strip() for _ in range(n)]
graph = [[] for _ in range(n)]

max_f = 0
for i in range(n):
    for j in range(n):
        if a[i][j] == 'Y':
            graph[i].append(j)

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
    return dist.count(1) + dist.count(2)
for i in range(n):
    dist = [-1] * n
    max_f = max(max_f, bfs(i))

print(max_f)