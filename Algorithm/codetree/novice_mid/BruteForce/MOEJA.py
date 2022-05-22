import sys

input = sys.stdin.readline

min_val = int(1e9)

n = int(input())
ls = list(map(int, input().split()))

for i in range(n):
    temp = 0
    for j in range(n):
        temp += abs(j - i) * ls[j]
    min_val = min(temp, min_val)

print(min_val)