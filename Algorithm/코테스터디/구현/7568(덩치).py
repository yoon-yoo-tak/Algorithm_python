"""
덩치
"""
import sys

input = sys.stdin.readline

t = int(input())
info = [list(map(int, input().split())) for _ in range(t)]
for man in info:
    rank = 1
    for other_man in info:
        if man[0] < other_man[0] and man[1] < other_man[1]:
            rank += 1
    print(rank, end=" ")
