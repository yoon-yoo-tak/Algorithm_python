"""

1253 좋다

"""
import sys
input = sys.stdin.readline

n = int(input())
a = sorted(map(int, input().split()))

def ok(idx):
    l, r = 0, n - 1
    target = a[idx]
    while l < r:
        if l == idx: l += 1
        elif r == idx: r -= 1
        else:
            if a[l] + a[r] > target:
                r -= 1
            elif a[l] + a[r] < target: l += 1
            else:
                return True
    return False

print(len([i for i in range(n) if ok(i)]))