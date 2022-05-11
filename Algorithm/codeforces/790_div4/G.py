from collections import deque
import sys

sys.setrecursionlimit(100000)


def dfs(cur, pre):
    for nex in g[cur]:
        if nex != pre:
            dfs(nex, cur)
            B[cur][0] += B[nex][0]
            B[cur][1] += B[nex][1]


for _ in range(int(input())):
    n = int(input())
    A = list(map(int, input().split()))
    g = [[] for i in range(n)]

    S = set()
    S.add(0)
    for i in range(1, n):
        # A[i-1],i
        A[i - 1] -= 1
        g[A[i - 1]].append(i)
        g[i].append(A[i - 1])
        S.add(A[i - 1])

    s = input()
    # [B,W]
    B = [[0, 0] for _ in range(n)]
    for x in range(n):
        if s[x] == 'B':
            B[x][0] = 1
        else:
            B[x][1] = 1

    dfs(0, -1)

    res = 0
    for x in range(n):
        if B[x][0] == B[x][1]:
            res += 1

    print(res)