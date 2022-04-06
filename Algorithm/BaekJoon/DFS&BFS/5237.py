"""
5237 - Connected or Not Connected

1. 아이디어
2. 시간복잡도
3. 자료구조
"""

import sys
from collections import deque
input = sys.stdin.readline
t = int(input())

def bfs(v):
    q = deque()
    q.append(v)
    visit[v] = True
    while q:
        node = q.popleft()
        for i in graph[node]:
            if not visit[i]:
                q.append(i)
                visit[i] = True


for _ in range(t):
    n, k, *a = map(int, input().split())
    graph = [[] for _ in range(n)]
    visit = [False] * n
    for i in range(0, len(a), 2):
        graph[a[i]].append(a[i + 1])
        graph[a[i + 1]].append(a[i])
    for i in range(n):
        visit = [False] * n
        bfs(i)
        if visit.count(False) > 0:
            print('Not connected.')
            break
        else:
            print('Connected.')
            break
