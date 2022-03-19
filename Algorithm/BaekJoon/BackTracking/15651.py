"""
15651 N과M(3)

1부터 N까지 중복허용 M개

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
        for i in range(1, n+1):
            sel[k] = i
            rec(k + 1)
            sel[k] = 0
rec(0)