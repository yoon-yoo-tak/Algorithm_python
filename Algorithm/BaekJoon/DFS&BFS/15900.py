"""
15900 나무 탈출

1. 아이디어
2. 시간복잡도
3. 자료구조
"""

import sys

input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n + 1)]
for i in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

stack = [[1, 0]]
visit = [0] * (n + 1)
visit[1] = -1

ls = []

while stack:
    curr, l = stack.pop()
    visit[curr] = 1

    if curr != 1 and len(graph[curr]) == 1:
        ls.append(l)
        continue
    for x in graph[curr]:
        if visit[x] == 0:
            stack.append([x, l + 1])
ls = sum(ls)

if ls % 2 == 0:
    print('No')
else:
    print('Yes')