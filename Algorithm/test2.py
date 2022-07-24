import sys
input = sys.stdin.readline

n = int(input())

a, b, c, d = [], [], [], []

for _ in range(n):
    q, w, e, r = map(int, input().split())
    a.append(q)
    b.append(w)
    c.append(e)
    d.append(r)
a.sort()
b.sort()
c.sort(reverse=True)
d.sort(reverse=True)
ab_sum = [i + j for i in b for j in a] + [2 ** 28 + 1]
cd_sum = [i + j for i in d for j in c] + [2 ** 28 + 1]
cd_sum.sort(reverse=True)

l, r = 0, 0
temp = n * n
ans = 0
while l < temp and r < temp:
    temp_sum = ab_sum[l] + cd_sum[r]
    if temp_sum == 0:
        x, y = ab_sum[l], cd_sum[r]
        p, q = l, r
        while x == ab_sum[l]:
            l += 1
        while y == cd_sum[r]:
            r += 1
        ans += (l - p) * (r - q)
    elif temp_sum < 0:
        l += 1
    else:
        r += 1
print(ans)

