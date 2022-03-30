"""

12761 돌다리

"""
import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    while q:
        x = q.popleft()
        for i in range(8):
            if i < 6:
                nx = x + dx[i]
                if 0 <= nx <= 100000 and not visit[nx]:
                    q.append(nx)
                    visit[nx] = True
                    dist[nx] = dist[x] + 1
            else:
                nx = x * dx[i]
                if 0 <= nx <= 100000 and not visit[nx]:
                    q.append(nx)
                    visit[nx] = True
                    dist[nx] = dist[x] + 1

a, b, n, m = map(int, input().split())

dist = [0] * 100001
visit = [False] * 100001
dx = [1, -1,a, -a, b, -b, a, b]
q = deque()
q.append(n)
visit[n] = True
bfs()
print(dist[m])