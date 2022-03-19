"""

15656 N과M(7)

N개중 M개 고르기 중복가능

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
        for i in range(n):
            sel[k] = ls[i]
            rec(k + 1)
            sel[k] = 0
rec(0)