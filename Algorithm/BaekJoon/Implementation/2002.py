"""
2002 추월

"""

import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
ans = 0
enter = defaultdict(int)
out = []
for i in range(n):
    a = input().strip()
    enter[a] = i
for _ in range(n):
    a = input().strip()
    out.append(a)
for i in range(n - 1):
    for j in range(i + 1, n):
        if enter[out[i]] > enter[out[j]]:
            ans += 1
            break
print(ans)
