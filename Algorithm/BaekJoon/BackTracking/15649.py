"""
15649 : N과M(1)

1부터 N까지 중복없이 M개 고르기
"""
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
sel = [0] * m
used = [False] * (n + 1)

def rec(k):
    if k == m:
        for x in sel:
            print(x, end=' ')
        print()
    else:
        for i in range(1, n + 1):
            if used[i]:
                continue
            sel[k] = i
            used[i] = True
            rec(k + 1)
            sel[k] = 0
            used[i] = False

