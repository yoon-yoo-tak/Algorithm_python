import sys

input = sys.stdin.readline

def fact(k):
    if k <= 1:
        return 1
    return fact(k - 1) * k

n = int(input())

print(fact(n))