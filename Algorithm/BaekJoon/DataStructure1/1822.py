"""
1822 차집합
"""
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
a = set(map(int, input().split()))
b = set(map(int, input().split()))
ans = sorted(a - b)
ll = len(ans)
print(ll)
if ll > 0:
    print(*ans)
