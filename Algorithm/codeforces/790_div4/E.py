import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, q = map(int, input().split())
    ls = sorted(map(int, input().split()), reverse=True)
    query = list(int(input().strip()) for _ in range(q))
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = dp[i - 1] + ls[i - 1]
    def bise(a, l, r, x):
        while l <= r:
            mid = (l + r) // 2
            if a[mid] >= x:
                result = mid
                r = mid - 1
            else:
                l = mid + 1
        return result
    for q in query:
        if dp[-1] < q:
            print(-1)
            continue
        ans = bise(dp, 1, n + 1, q)
        print(ans)

