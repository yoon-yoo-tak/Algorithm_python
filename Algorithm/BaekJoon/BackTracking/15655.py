"""

15655 N과M(6)

N개중에 M개, 중복없이 오름차순

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
            if k==0 or sel[k-1] < ls[i]:
                sel[k] = ls[i]
                rec(k + 1)
                sel[k] = 0

rec(0)
