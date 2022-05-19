import sys

input = sys.stdin.readline

def recur(k):
    if k == 0:
        return
    print(k, end=' ')
    recur(k - 1)
    print(k, end=' ')

n = int(input())

recur(n)
