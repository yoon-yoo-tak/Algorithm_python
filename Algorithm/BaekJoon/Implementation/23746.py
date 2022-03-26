"""

23746 문자열 압축 해제

"""
import sys
input = sys.stdin.readline

n = int(input())
a = []
for i in range(n):
    b, c = input().split()
    a.append((b,c))

s = input().strip()

for i in s:
    for j in range(n):
        if i == a[j][1]:
            s = s.replace(i, a[j][0])

st, e = map(int, input().split())
print(s[st-1:e])