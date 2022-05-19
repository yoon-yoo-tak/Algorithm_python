import sys

input = sys.stdin.readline

offset = 100
n = int(input())
ls = [0] * 201

for _ in range(n):
    a, b = map(int, input().split())
    a, b = a + offset, b + offset
    for i in range(a, b):
        ls[i] += 1

print(max(ls))