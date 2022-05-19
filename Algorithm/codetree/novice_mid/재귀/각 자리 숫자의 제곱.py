import sys

input = sys.stdin.readline

def recur(k):
    if k < 10:
        return k ** 2
    return recur(k // 10) + ((k % 10) ** 2)


n = int(input())

print(recur(n))