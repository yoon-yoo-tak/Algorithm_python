"""
10816 숫자 카드 2
-10 -10 2 3 3 7 6 10 10

10
"""
import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

n = int(input())
a = sorted(map(int, input().split()))
m = int(input())
for i in list(map(int, input().split())):
    print(bisect_right(a, i) - bisect_left(a, i), end=' ')