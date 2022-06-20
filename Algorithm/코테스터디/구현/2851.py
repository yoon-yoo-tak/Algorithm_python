"""
2851 수퍼 마리오
"""
import sys

input = sys.stdin.readline


mus = [int(input()) for _ in range(10)]
result = 0
for i in range(len(mus)):
    result += mus[i]
    if result >= 100:
        before = abs(result-mus[i]-100)
        now = abs(result-100)
        if now > before:
            print(result - mus[i])
            break
        else:
            print(result)
            break
    if i==len(mus)-1 and result<100:
        print(result)