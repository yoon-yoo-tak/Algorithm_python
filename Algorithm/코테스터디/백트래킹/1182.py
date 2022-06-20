n, s = map(int, input().split())
ls = list(map(int, input().split()))
ans = 0

def rec(k, val):
    global ans
    if k == n:
        if val == s:
            ans += 1
    else:
        rec(k + 1, val + ls[k])
        rec(k + 1, val)

rec(0, 0)
if s == 0:
    ans -= 1
print(ans)