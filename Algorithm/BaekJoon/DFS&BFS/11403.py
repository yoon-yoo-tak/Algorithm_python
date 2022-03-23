"""

11403 경로 찾기

"""
import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
adj = [list(map(int, input().split())) for _ in range(n)]

def bfs(x):
    visit = [0] * n
    queue = deque()
    queue.append(x)
    while queue:
        x = queue.popleft()
        for y in range(n):
            if not adj[x][y] or visit[y]:
                continue
            visit[y] = 1
            queue.append(y)
    for i in range(n):
        print(visit[i], end=' ')
    print()

for i in range(n):
    bfs(i)