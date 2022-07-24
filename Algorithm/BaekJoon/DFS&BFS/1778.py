"""
1778 Ubiquitous Religions
연결요소의 갯수 찾기
"""
import sys
from collections import deque
input = sys.stdin.readline

def bfs(x):
    q = deque()
    q.append(x)
    visited[x] =True
    while q:
        x = q.popleft()
        for i in graph[x]:
            if not visited[i]:
                q.append(i)
                visited[i] = True

num = 1
while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    visited = [False] * (n + 1)
    cnt = 0
    for i in range(1, n + 1):
        if not visited[i]:
            bfs(i)
            cnt += 1
    print(f'Case {num}: {cnt}')
    num += 1
