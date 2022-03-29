"""

20362 유니대전 퀴즈쇼

"""
import sys
input = sys.stdin.readline

a, b = input().split()
ls = dict()
for _ in range(int(a)):
    name, answer = input().split()
    ls[name] = answer

corr = ls[b]
count = 0
for i in ls:
    if i == b and ls[i] == corr:
        break
    if i != b and ls[i] == corr:
        count += 1


print(count)