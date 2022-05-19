import sys

input = sys.stdin.readline

def star(k):
    if k == 0:
        return
    star(k - 1)
    print('*' * k)

n = int(input())

star(n)