"""
9489 사촌
"""
import sys

input = sys.stdin.readline

while True:
    n, K = map(int, input().split())
    if n == 0 and K == 0: break
    a = [0] + list(map(int, input().split()))

    parent = [0] * (n + 1)
    parent[0] = -1

    last = 1
    i = 2
    while i <= n:
        while i <= n:
            parent[i] = last
            if i < n and a[i] + 1 != a[i + 1]:
                break
            i += 1
        i += 1
        last += 1

    idx_k = 0
    for i in range(1, n + 1):
        if a[i] == K:
            idx_k = i

    ans = 0
    for i in range(1, n + 1):
        if parent[parent[i]] == parent[parent[idx_k]] and parent[i] != parent[idx_k]:
            ans += 1
    print(ans)
