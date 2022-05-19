import sys

input = sys.stdin.readline

def hap(k):
    if k == 1:
        return 1
    return hap(k - 1) + k

n = int(input())
print(hap(n))