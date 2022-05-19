import sys

input = sys.stdin.readline

n, k = map(int, input().split())
ls = [0] * (n + 1)
for i in range(k):
    a, b = map(int, input().split())
    for j in range(a, b + 1):
        ls[j] += 1

print(max(ls))
