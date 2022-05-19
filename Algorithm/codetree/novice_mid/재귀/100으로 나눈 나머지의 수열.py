
import sys

input = sys.stdin.readline

def rec(k):
    if k == 1:
        return 2
    if k == 2:
        return 4
    return (rec(k - 1) * rec(k - 2)) % 100

n = int(input())

print(rec(n))