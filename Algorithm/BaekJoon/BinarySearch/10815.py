"""

10815 숫자 카드


"""
import sys
input = sys.stdin.readline

n = int(input())
a = sorted(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
ls = []
def bise(a, l, r, x):
    while l <= r:
        mid = (l + r) //2
        if a[mid] == x:
            return True
        if a[mid] < x: l = mid + 1
        else: r = mid - 1
    return False
for i in b:
    print(1 if bise(a, 0, n - 1, i) else 0, end=' ')


