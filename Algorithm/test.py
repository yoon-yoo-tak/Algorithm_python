import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

sel = [0 for _ in range(m)]
used = [0 for _ in range(n + 1)]
def dfs(k):
    if k == m:
        for i in sel:
            print(i, end=' ')
        print()
    else:
        start = 1 if k == 0 else sel[k - 1] + 1
        for i in range(start, n + 1):
            sel[k] = i
            used[i] = 1
            dfs(k + 1)
            sel[k] = 0
            used[i] = 0


dfs(0)