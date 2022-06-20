"""
베스트셀러
"""
import sys
from collections import defaultdict
input = sys.stdin.readline

books = defaultdict(int)

for _ in range(int(input())):
    books[input().strip()] += 1

best = sorted([[i, books[i]] for i in books], key=lambda x:(-x[1], x[0]))

print(best[0][0])
