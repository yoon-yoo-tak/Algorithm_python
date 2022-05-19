import sys

input = sys.stdin.readline

def recur(k):
    if k == 1:
        return 1
    if k == 2:
        return 2
    return recur(k - 2) + k

n = int(input())
print(recur(n))
