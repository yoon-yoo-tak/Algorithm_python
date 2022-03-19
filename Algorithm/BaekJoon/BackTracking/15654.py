"""
15654 N과M(5)

N개중에 중복없이 M개 뽑기
"""
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
ls = sorted(map(int, input().split()))

sel = [0 for _ in range(m)]
used = [0 for _ in range(n+1)]
def rec(k):
    if k == m:
        for x in sel:
            print(x, end=' ')
        print()
    else:
        for i in range(len(ls)):
            if used[i]:
                continue
            sel[k] = ls[i]
            used[i] = 1
            rec(k + 1)
            sel[k] = 0
            used[i] = 0
rec(0)
