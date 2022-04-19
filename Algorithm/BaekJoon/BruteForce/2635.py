"""
2635 수 이어가기

"""
import sys

input = sys.stdin.readline
n = int(input())
if n % 2 == 0:
    target = n // 2
else:
    target = (n // 2) + 1
result = []

ls = [n]
for i in range(target, n + 1):
    ls.append(i)
    while True:
        temp = ls[-2] - ls[-1]
        if temp < 0:
            break
        ls.append(temp)
    result.append((len(ls), ls))
    ls = [n]
result.sort(key=lambda x:-x[0])
print(result[0][0])
print(*result[0][1])