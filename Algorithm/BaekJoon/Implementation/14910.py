"""

14910 오르막

비내림차순인지 확인

"""
import sys
input = sys.stdin.readline
a = list(map(int, input().split()))
b = 1
for i in range(len(a)-1):
    if a[i] > a[i + 1]:
        b = 0
print("Bad" if b == 0 else "Good")


