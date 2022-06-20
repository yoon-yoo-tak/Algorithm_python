"""
7511 소셜 네트워킹 어플리케이션
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

t = int(input())
for tt in range(1, t + 1):
    n = int(input())
    k = int(input())
    parent = [i for i in range(n)]

    for _ in range(k):
        a, b = map(int, input().split())
        union(a, b)
    m = int(input())
    print(f'Scenario {tt}:')
    for _ in range(m):
        a, b = map(int, input().split())
        print(1 if find(a) == find(b) else 0)
    if tt != t:
        print()
