"""

15665 N과M(11)

N개중 M개 같은 수여러번 골라도 됨

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
            sel[k] = ls[i]
            remember = ls[i]
            rec(k + 1)
            sel[k] = 0
rec(0)