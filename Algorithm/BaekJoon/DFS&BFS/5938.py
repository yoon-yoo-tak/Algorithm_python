"""
5938 - Daisy Chains in the Field

1. 아이디어
2. 시간복잡도
3. 자료구조
"""

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visit = [False] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

q = deque()
q.append(1)
visit[1] = True
while q:
    a = q.popleft()
    for i in graph[a]:
        if not visit[i]:
            q.append(i)
            visit[i] = True
if False in visit[1:]:
    for i in range(1, n + 1):
        if not visit[i]:
            print(i)
else:
    print(0)
