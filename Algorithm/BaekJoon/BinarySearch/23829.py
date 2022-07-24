"""
23829 인문예술탐사주간
"""

import sys
input = sys.stdin.readline

def bisect(a, l, r, x):  # 작은값 찾기
    ans = -1
    while l <= r:
        mid = (l + r) // 2
        if a[mid] < x:
            ans = mid
            l = mid + 1
        else:
            r = mid - 1
    return ans



n, q = map(int, input().split())
tree = sorted(map(int, input().split()))
prefix_sum = [0] * n
prefix_sum[0] = tree[0]
for i in range(1, n):
    prefix_sum[i] = prefix_sum[i - 1] + tree[i]
for _ in range(q):
    spot = int(input())
    idx = bisect(tree, 0, n - 1, spot)
    if idx == -1:
        ans = prefix_sum[n - 1] - (spot * n)
    elif idx == n - 1:
        ans = (spot * n) - prefix_sum[n - 1]
    else:
        bigger = (prefix_sum[-1] - prefix_sum[idx]) - spot * (n - idx - 1)
        smaller = (spot * (idx + 1)) - prefix_sum[idx]
        ans = bigger + smaller

    print(ans)



