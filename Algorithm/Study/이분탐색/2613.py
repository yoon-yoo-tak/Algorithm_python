"""
2613 숫자 구슬
"""
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
ls = list(map(int, input().split()))

ans = 0
ans_ls = []
l, r = max(ls), sum(ls)
while l <= r:
    mid = (l + r) // 2
    cnt = 0
    idx = 0
    ans_ls = []
    while idx < n:
        temp_sum = 0
        temp_cnt = 0
        while idx < n and temp_sum + ls[idx] <= mid:
            temp_sum += ls[idx]
            temp_cnt += 1
            idx += 1
            if m - cnt == n - (idx - 1):
                break
        cnt += 1
        ans_ls.append(temp_cnt)
    if cnt > m:
        l += 1
    else:
        r -= 1
    ans = mid

print(ans)
print(*ans_ls)
