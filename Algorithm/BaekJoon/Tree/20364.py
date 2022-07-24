"""
20364 부동산 다툼
"""
import sys

input = sys.stdin.readline

n, q = map(int, input().split())
visited = [False] * (n + 1)
for _ in range(q):
    x = int(input())
    y = x
    ans = 0
    while x:
        if visited[x]:
            ans = x
        x //= 2
    visited[y] = True
    print(ans)
