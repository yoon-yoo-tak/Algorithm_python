"""
9940 순열1
"""
t = int(input())
for tt in range(t):
    n = int(input())
    ls = list(map(int, input().split()))
    flag = True
    for i in range(1, n + 1):
        if ls.count(i) != 1:
            flag = False
            break
    if flag:
        ans = 'Yes'
    else:
        ans = 'No'
    print(f'#{tt + 1} {ans}')