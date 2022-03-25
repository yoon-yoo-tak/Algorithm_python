"""

24444 알고리즘 수업 - 너비 우선 탐색 1

"""
import sys
from collections import deque
input = sys.stdin.readline

n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visit = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def bfs(v):
    q = deque()
    q.append(v)
    visit[v] = True
    while q:
        n = q.popleft()
        print(n)
        for i in graph[n]:
            if not visit[i]:
                q.append(i)
                visit[i] = True

bfs(v)
