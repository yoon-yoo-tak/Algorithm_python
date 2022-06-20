"""
1939 중량제한
"""
import sys

input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a, b = find(a), find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b




n, m = map(int, input().split())
parent = [i for i in range(n + 1)]
graph = []
for _ in range(m):
    a, b, c = map(int, input().split())
    graph.append([-c, a, b])
x, y = map(int, input().split())
graph.sort()

for c, a, b in graph:
    c = abs(c)
    union(a, b)
    if find(x) == find(y):
        print(c)
        break