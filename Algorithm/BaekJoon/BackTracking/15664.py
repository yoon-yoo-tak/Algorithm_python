"""
15664 N과M(10)

N개중에 M개 비내림차순
"""

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
ls = sorted(map(int, input().split()))

sel = [0 for _ in range(m)]
used = [0 for _ in range(n + 1)]

def rec(k):
    if k == m:
        for x in sel:
            print(x, end=' ')
        print()
    else:
        remember = 0
        for i in range(n):
            if used[i] or ls[i] == remember:
                continue
            if k == 0 or sel[k-1] <=ls[i]:
                sel[k] = ls[i]
                remember = ls[i]
                used[i] = 1
                rec(k + 1)
                sel[k] = 0
                used[i] = 0
rec(0)