
import sys

input = sys.stdin.readline

def rec(k):
    if k < 10:
        return k
    return rec(k // 10) + (k % 10)


a, b, c = map(int, input().split())

print(rec(a * b * c))