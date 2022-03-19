"""
15649 : N과M(1)

1부터 N까지 중복없이 M개 고르기
"""
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
sel = [0 for _ in range(m)]
used = [0 for _ in range(n+1)]
def rec(k):
    # k 가 m이다?  >> m개만큼 골랐다.
    if k == m:
        for x in sel:
            print(x, end=' ')
        print()
    else:
        for i in range(1, n+1):
            if used[i]:
                continue
            sel[k] = i
            used[i] = 1
            rec(k + 1)
            sel[k] = 0
            used[i] = 0
rec(0)
