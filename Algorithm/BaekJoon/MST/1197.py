"""
최소 스패닝 트리
"""
import sys

input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


v, e = map(int, input().split())
parent = [i for i in range(v + 1)]
edges = sorted([list(map(int, input().split())) for _ in range(e)], key=lambda x:x[2])
ans = 0

for a, b, cost in edges:
    if find(a) != find(b):
        union(a, b)
        ans += cost

print(ans)