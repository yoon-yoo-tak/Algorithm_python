import sys

input = sys.stdin.readline

a, b = map(int, input().split())
ls = []
while a > 0:
    ls.append(a % b)
    a //= b
for i in ls[::-1]:
    print(i,end='')

