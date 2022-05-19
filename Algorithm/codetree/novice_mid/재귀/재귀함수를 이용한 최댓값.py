
import sys

input = sys.stdin.readline


def rec(k):
    if k == 0:
        return ls[0]
    return max(rec(k - 1), ls[k])


n = int(input())
ls = list(map(int, input().split()))

print(rec(n - 1))