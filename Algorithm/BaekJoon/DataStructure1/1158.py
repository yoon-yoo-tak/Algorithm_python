"""
1158 요세푸스 문제


"""

import sys

input = sys.stdin.readline

n, k = map(int, input().split())
ls = [i + 1 for i in range(n)]
idx = 0
ls1 = []
for _ in range(n):
    idx += k - 1
    if idx >= len(ls):
        idx %= len(ls)

    ls1.append(str(ls.pop(idx)))

print('<',', '.join(ls1),'>', sep='')





