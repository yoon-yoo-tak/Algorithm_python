"""
15650 N과M(2)

1부터 n까지 중복없이 m개, 오름차순
"""
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
sel = [0 for _ in range(m)]
used = [0 for _ in range(n+1)]
def rec(k):
    if k == m:
        for x in sel:
            print(x, end=' ')
        print()
    else:
        start = 1 if k==0 else sel[k-1]+1
        for i in range(start, n+1):
            if used[i]:
                continue
            sel[k] = i
            used[i] = 1
            rec(k + 1)
            sel[k] = 0
            used[i] = 0
rec(0)
