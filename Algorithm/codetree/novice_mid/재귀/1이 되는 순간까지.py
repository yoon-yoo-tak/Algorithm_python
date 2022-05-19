import sys

input = sys.stdin.readline

def recurr(k):
    if k == 1:
        return 0
    if k % 2 == 0:
        return recurr(k // 2) + 1
    else:
        return recurr(k // 3) + 1


n = int(input())
print(recurr(n))