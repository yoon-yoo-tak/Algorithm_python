"""
개발자의 능력 3
"""
import sys

input = sys.stdin.readline

n = 6
m_val = int(1e9)
ls = list(map(int, input().split()))

def diff(i, j, k):
    sum1 = ls[i] + ls[j] + ls[k]
    sum2 = sum(ls) - sum1
    return abs(sum1 - sum2)

min_val = m_val

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            min_val = min(min_val, diff(i, j, k))
print(min_val)