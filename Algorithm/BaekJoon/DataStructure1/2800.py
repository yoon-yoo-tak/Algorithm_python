"""
2800 괄호 제거

1. 아이디어
2. 시간복잡도
3. 자료구조
"""

import sys
from itertools import combinations
input = sys.stdin.readline

problem = [*input().strip()]
p, idx_brs = [],[]
for i,v in enumerate(problem):
    if v == '(':
        problem[i] = ''
        p += [i]
    if v == ')':
        problem[i] = ''
        idx_brs += [[p.pop(), i]]
out = set()
for i in range(len(idx_brs)):
    for j in combinations(idx_brs, i):
        P = problem[:]
        for v, w in j:
            P[v] = '('
            P[w] = ')'
        out.add(''.join(P))
for i in sorted(out):
    print(i)

