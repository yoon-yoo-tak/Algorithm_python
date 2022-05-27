"""
컨베이어 벨트
"""
import sys

input = sys.stdin.readline

n, t = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

for _ in range(t):
    temp_a = a[-1]
    temp_b = b[-1]
    for i in range(n - 1, 0, -1):
        a[i] = a[i - 1]
        b[i] = b[i - 1]
    a[0] = temp_b
    b[0] = temp_a

print(*a)
print(*b)
