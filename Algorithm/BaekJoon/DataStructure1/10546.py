"""
10546 배부른 마라토너
"""
import sys
from collections import defaultdict
input = sys.stdin.readline

parti = defaultdict(int)
n = int(input())
for _ in range(n):
    parti[input().strip()] += 1
for _ in range(n - 1):
    parti[input().strip()] -= 1

for i in parti:
    if parti[i]:
        print(i)
        break
