"""
17352 여러분의 다리가 되어 드리겠습니다!
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


n = int(input())
parent = [i for i in range(n + 1)]
for _ in range(n - 2):
    a, b = map(int, input().split())
    union(a, b)

q = find(1)
for i in range(2, n + 1):
    if q != find(i):
        print(q, i)
        sys.exit()


