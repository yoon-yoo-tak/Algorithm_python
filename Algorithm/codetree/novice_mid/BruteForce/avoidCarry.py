"""
Carry 피하기 2
"""
import sys

input = sys.stdin.readline


def is_carry(a, b, c):
    al, bl, cl = len(a), len(b), len(c)
    d = max(al, bl, cl)
    a = '0' * (d - al) + a
    b = '0' * (d - bl) + b
    c = '0' * (d - cl) + c
    a, b, c = a[::-1], b[::-1], c[::-1]

    for i in range(d):
        if int(a[i]) + int(b[i]) + int(c[i]) >= 10:
            return False
    return True


n = int(input())
ls = [input().strip() for _ in range(n)]
ans = -1
for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            if is_carry(ls[i], ls[j], ls[k]):
                ans = max(ans, int(ls[i]) + int(ls[j]) + int(ls[k]))

print(ans)