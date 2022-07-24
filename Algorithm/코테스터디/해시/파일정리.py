import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
h = defaultdict(int)
for _ in range(n):
    b = input().split('.')[1]
    h[b] += 1

sorting = sorted(h.items())
for key, value in sorting:
    print(key.strip(), value)