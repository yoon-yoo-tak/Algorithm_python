"""
1835 카드
"""
import sys

input = sys.stdin.readline

n = int(input())
l = [n]
for i in range(n-1,0,-1):
    l = [i]+l
    for j in range(i):
        l = l[n-i:] + l[0:n-i]
for i in range(n):
    print(l[i],end=' ')