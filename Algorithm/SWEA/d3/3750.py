"""
3750 Digit Sum
"""
res = [0]
for tt in range(1, int(input()) + 1):
    n = int(input())
    ans = str(n)
    while len(ans) > 1:
        temp = sum([int(i) for i in ans])
        ans = str(temp)
    res.append(int(''.join(ans)))

for i in range(1, len(res)):
    print(f'#{i} {res[i]}')
