
import sys

input = sys.stdin.readline

def rec(k):
    if k == 1:
        return 0
    if k % 2 == 0:
        return rec(k // 2) + 1
    else:
        return rec(k * 3 + 1) + 1


n = int(input())

print(rec(n))