"""
1068 트리
작은 문제를 이용해 큰 문제를 해결하자.
subtree 활용
"""

import sys

input = sys.stdin.readline

n = int(input())
parent = list(map(int, input().split()))
child = [[] for _ in range(n)]
leaf = [0] * n
erased = int(input())
root = 0
for i in range(n):
    if parent[i] == -1:
        root = i
    else:
        if erased == i:
            continue
        child[parent[i]].append(i)

def dfs(x, par):
    if not child[x]:
        leaf[x] = 1
    for y in child[x]:
        if y == par:
            continue
        dfs(y, x)
        leaf[x] += leaf[y]

if root != erased:
    dfs(root, -1)
print(leaf[root])


