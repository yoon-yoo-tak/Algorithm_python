"""
13549 숨바꼭질 3

1. 아이디어
2. 시간복잡도
3. 자료구조
"""

import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
maxVal = 100000
dist = [-1] * (maxVal + 1)

def bfs(x):
    q = deque([x])
    dist[x] = 0
    while q:
        x = q.popleft()
        if 0 <= x - 1 < 100001 and dist[x - 1] == -1:
            dist[x - 1] = dist[x] + 1
            q.append((x - 1))
        if 0 < x * 2 < 100001 and dist[x * 2] == -1:
            dist[x * 2] = dist[x]
            q.appendleft(x * 2)
        if 0 <= x + 1 < 100001 and dist[x + 1] == -1:
            q.append((x + 1))
            dist[x + 1] = dist[x] + 1

bfs(n)
print(dist[k])
