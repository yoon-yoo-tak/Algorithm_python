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

for i in graph:
    i.sort()

ls = [-1] * (n + 1)


def bfs(v, cnt):
    q = deque()
    q.append((v, cnt))
    visit[v] = True
    while q:
        x, cnt = q.popleft()
        for i in graph[x]:
            if not visit[i]:
                q.append((i, cnt + 1))
                ls[cnt] = x
                visit[i] = True


bfs(v, 1)
for i in ls[1:]:
    print(i if i != -1 else 0)