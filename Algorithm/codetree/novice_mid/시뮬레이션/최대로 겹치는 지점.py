import sys

input = sys.stdin.readline

ls = [0] * 101

n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    for i in range(a, b + 1):
        ls[i] += 1

print(max(ls))
