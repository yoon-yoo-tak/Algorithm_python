"""
20955 민서의 응급수술
사이클이다 > 간선 하나제거
부모가 다르다 > 연결
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
ans = 0
parent = [i for i in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    if find(u) == find(v):
        ans += 1
    union(u, v)
for i in range(1, n):
    if find(i) != find(i + 1):
        union(i, i + 1)
        ans += 1
print(ans)