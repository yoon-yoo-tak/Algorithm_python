"""

3273 두 수의 합

ai + aj = x 인 (ai, aj) 쌍의 갯수 출력

이분탐색으로 어떻게?

목표값 X
정렬 해서 처음 값부터 나머지 값에 대해 X-a[j] = a[i] 인 값 찾아서 있으면  count++

"""
import sys
input = sys.stdin.readline

n = int(input())
a = sorted(map(int, input().split()))
x = int(input())

def bise(a, l, r, x):
    while l <= r:
        mid = (l + r) // 2
        if a[mid] == x:
            return True
        if a[mid] < x: l = mid + 1
        else: r = mid - 1
count = 0
for i in range(len(a)):
    target = abs(x-a[i])
    if bise(a, i+1, n-1, target): count += 1
print(count)