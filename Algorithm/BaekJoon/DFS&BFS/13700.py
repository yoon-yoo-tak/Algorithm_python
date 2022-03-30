"""

13700 완전 범죄

"""
import sys
from collections import deque
input = sys.stdin.readline

n, s, d, f, b, k = map(int, input().split())
a = list(map(int, input().split()))

def bfs():
    q = deque()
    q.append(s)
    dist[s] = 0
    while q:
        x = q.popleft()
        if x == d:
            print(dist[x])
            return
        for nx in (x + f), (x - b):
            if 1 <= nx <= 1e5 and nx not in dist:
                q.append(nx)
                dist[nx] = dist[x] + 1
    print('BUG FOUND')

dist = dict()
for i in range(k):
    dist[a[i]] = 0
bfs()