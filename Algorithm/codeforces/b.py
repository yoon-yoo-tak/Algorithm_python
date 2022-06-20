"""

"""
import sys

input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    ls = list(map(int, input().split()))
    temp = set(ls)
    ll = len(ls)
    if len(ls) == len(temp):
        print(len(ls))
        continue
    else:
        while ll > len(temp):
            ll -= 2
        print(ll)