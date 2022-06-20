import sys
from collections import Counter
input=sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
a_sort = sorted(set(a))

dic = {a_sort[i]: i for i in range(len(a_sort))}
for i in a:
    print(dic[i], end=' ')

