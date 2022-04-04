"""
21937 작업

1. 아이디어
2. 시간복잡도
3. 자료구조
"""

import sys
from collections import deque
input = sys.stdin.readline


def bfs(x):
    q = deque([x])
    visit[x] = True
    while q:
        x = q.popleft()
        for i in graph[x]:
            if not visit[i]:
                q.append(i)
                visit[i] = True


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visit = [False] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)

t = int(input())
bfs(t)
print(visit.count(True) - 1)
