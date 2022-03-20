"""

15666 N과M(12)

N개중 M개 중복허용 비내림차순
"""
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
ls = sorted(map(int, input().split()))

sel = [0 for _ in range(m)]

def rec(k):
    if k == m:
        for x in sel:
            print(x, end=' ')
        print()
    else:
        remember = 0
        for i in range(n):
            if remember == ls[i]:
                continue
            if k ==0 or sel[k-1] <= ls[i]:
                sel[k] = ls[i]
                remember = ls[i]
                rec(k + 1)
                sel[k] = 0
rec(0)
