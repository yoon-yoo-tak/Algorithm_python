import sys

input = sys.stdin.readline

def fibbo(n):
    if n <= 2:
        return 1
    return fibbo(n - 1) + fibbo(n - 2)


n = int(input())
print(fibbo(n))