"""

14562 태권왕



"""
import sys
from collections import deque

input = sys.stdin.readline

def bfs(s, t):
    q = deque()
    q.append((s, t, 0))
    dist = [-1] * 200
    while q:
        n, t, c = q.popleft()
        if n <= t and dist[n] == -1:
            q.append((n * 2, t + 3, c + 1))
            q.append((n + 1, t, c + 1))
            if n == t:
                return c


for _ in range(int(input())):
    s, t = map(int, input().split())
    print(bfs(s, t))