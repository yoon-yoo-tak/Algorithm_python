"""
여행 가자
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
    elif a > b:
        parent[a] = b
    else:
        return


n = int(input())
parent = [i for i in range(n + 1)]
m = int(input())
for i in range(1, n + 1):
    info = list(map(int, input().split()))
    for k in range(1, len(info) + 1):
        if info[k - 1] == 1:
            union(i, k)
plan = list(map(int, input().split()))
res = [find(i) for i in plan]
print('YES' if len(set(res)) == 1 else 'NO')



