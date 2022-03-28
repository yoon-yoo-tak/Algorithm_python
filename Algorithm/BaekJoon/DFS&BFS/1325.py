"""

1325 효율적인 해킹

"""
import sys
from collections import deque
input = sys.stdin.readline


def bfs(v):
    cnt = 0
    q = deque()
    q.append(v)
    visit = [False] * (n + 1)
    visit[v] = True
    while q:
        node = q.popleft()
        cnt += 1
        for i in graph[node]:
            if not visit[i]:
                q.append(i)
                visit[i] = True
    return cnt


n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)

max_cnt = 0
res = []

for i in range(1, n + 1):
    if graph[i]:
        tmp = bfs(i)
        if max_cnt <= tmp:
            if max_cnt < tmp:
                res = []
            max_cnt = tmp
            res.append(i)
print(*res)
