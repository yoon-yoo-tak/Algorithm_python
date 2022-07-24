"""
3584 가장 가까운 공통 조상
"""
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    parent = [0] * (n + 1)
    for _ in range(n - 1):
        a, b = map(int, input().split())
        parent[b] = a
    visited = [False] * (n + 1)
    x, y = map(int, input().split())
    while x:
        visited[x] = True
        x = parent[x]

    while y and not visited[y]:
        y = parent[y]
    print(y)