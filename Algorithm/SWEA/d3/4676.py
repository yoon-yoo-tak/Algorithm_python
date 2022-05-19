"""
4676 늘어지는 소리 만들기
"""
for tt in range(1, int(input()) + 1):
    s = list(input())
    num = int(input())
    pos = list(map(int, input().split()))
    for i in pos:
        if i == 0:
            s[i] = '-' + s[i]
        elif i == len(s):
            s[-1] += '-'
        else:
            s[i] = '-' + s[i]
    ans = ''.join(s)
    print(f'#{tt} {ans}')
