"""
카드 정렬하기
백준 1715
"""

import sys
import heapq
input = sys.stdin.readline

n = int(input())
heap = []
for i in range(n):
    a = int(input())
    heapq.heappush(heap, a)

res = 0

while len(heap) != 1:
    first = heapq.heappop(heap)
    second = heapq.heappop(heap)

    val = first + second
    res += val
    heapq.heappush(heap, val)

print(res)
