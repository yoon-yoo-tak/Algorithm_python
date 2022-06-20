"""
24391 귀찮은 해강이
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

for _ in range(m):
    a, b = map(int, input().split())
    union(a, b)

ls = list(map(int, input().split()))
cnt = 0
for i in range(1, len(ls)):
    if find(ls[i]) != find(ls[i - 1]):
        cnt += 1
print(cnt)