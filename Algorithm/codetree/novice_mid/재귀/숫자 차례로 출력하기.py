import sys

input = sys.stdin.readline

def recur(k):
    if k == 0:
        return
    recur(k - 1)
    print(k, end= ' ')

def recur1(k):
    if k == 0:
        return
    print(k, end= ' ')
    recur1(k - 1)

n = int(input())

recur(n)
print()
recur1(n)