"""
16940 BFS 스페셜 저지

"""

import sys
from collections import deque, defaultdict
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)


for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

ls = list(map(int, input().split()))
child = defaultdict(list)


def bfs(v):
    q = deque()
    q.append(v)
    visited[v] = True
    while q:
        x = q.popleft()
        for i in graph[x]:
            if not visited[i]:
                q.append(i)
                child[x].append(i)
                visited[i] = True

if ls[0] != 1:
    print(0)
else:
    bfs(1)
    q = deque()
    q.append(1)
    idx = 1
    while q:
        tmp = q.popleft()
        a = set(child[tmp])
        a_len = len(a)
        b = ls[idx:idx + a_len]
        q.extend(b)
        b = set(b)
        idx += a_len
        if a != b:
            print(0)
            break
    else:
        print(1)



