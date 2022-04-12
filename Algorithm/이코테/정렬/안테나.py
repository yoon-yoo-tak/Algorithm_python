"""
안테나
백준 18310
"""

import sys

input = sys.stdin.readline
n = int(input())
print(sorted(map(int, input().split()))[(n - 1) // 2])