"""

2559 수열

"""
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
a = list(map(int, input().split()))
res = sum(a[:k])
maxv = res
for i in range(k, n):
    res += a[i]
    res -= a[i-k]
    maxv = max(maxv, res)
print(maxv)
