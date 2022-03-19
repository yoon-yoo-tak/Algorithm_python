"""
15652 N과M(4)

1부터 N까지 중복허용, 비내림차순 M개 뽑기

"""
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

sel = [0 for _ in range(m)]
def rec(k):
    if k == m:
        for x in sel:
            print(x, end=' ')
        print()
    else:
        start = 1 if k==0 else sel[k-1]
        for i in range(start, n+1):
            sel[k] = i
            rec(k + 1)
            sel[k] = 0
rec(0)
