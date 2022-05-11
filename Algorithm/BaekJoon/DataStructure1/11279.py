"""
11279 최대 힙
1927 최소 힙
11286 절댓값 힙
"""
import sys,heapq
input = sys.stdin.readline

q = []
for _ in range(int(input())):
    n = int(input())
    if n == 0:
        if len(q) == 0:
            print(0)
        else:
            print(heapq.heappop(q)[1])
    else:
        heapq.heappush(q, (abs(n), n))
