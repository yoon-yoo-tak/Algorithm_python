import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
dist = [-1] * 100001


def bfs(n):
    q = deque()
    q.append(n)
    dist[n] = 0
    while q:
        n = q.popleft()
        for i in (n + 1, n - 1, n * 2):
            if i < 0 or i > 100000:
                continue
            if dist[i] != -1:
                continue
            q.append(i)
            dist[i] = dist[n] + 1
bfs(n)
print(dist[k])



