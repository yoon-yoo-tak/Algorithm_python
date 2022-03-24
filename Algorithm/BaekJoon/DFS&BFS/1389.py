"""

1389 케빈 베이컨의 6단계 법칙


"""
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def bfs(v):
    dist = [-1] * (n + 1)
    ret = 0
    q = deque()
    q.append(v)
    dist[v] = 0
    while q:
        x = q.popleft()
        ret += dist[x]
        for i in graph[x]:
            if dist[i] != -1:
                continue
            q.append(i)
            dist[i] = dist[x] + 1
    return ret

min_val, min_idx = bfs(1), 1
for i in range(2, n + 1):
    v = bfs(i)
    if min_val > v:
        min_val, min_idx = v, i

print(min_idx)
