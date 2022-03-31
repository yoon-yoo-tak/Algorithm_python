"""
5014 스타트링크


"""

import sys
from collections import deque
input = sys.stdin.readline

# f : 총 층, s : 현재 층, g : 목표 층
f, s, g, u, d = map(int, input().split())

dist = [-1] * f
visit = [False] * f
dist[s - 1] = 0
def bfs(x):
    q = deque()
    q.append(x)
    visit[x] = True
    while q:
        n = q.popleft()
        for ny in (n + u), (n - d):
            if ny < 0 or ny >= f:
                continue
            if visit[ny]:
                continue
            q.append(ny)
            dist[ny] = dist[n] + 1
            visit[ny] = True
bfs(s - 1)
print(dist[g - 1] if dist[g - 1] != -1 else 'use the stairs')