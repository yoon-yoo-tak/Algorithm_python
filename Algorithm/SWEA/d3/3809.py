"""
3809 화섭이의 정수 나열
"""
t = int(input())
for tt in range(1, t + 1):
    n = int(input())
    s = ''
    while True:
        s += ''.join(input().split())
        if len(s) == n:
            break
    temp = 0
    ans = 0
    while True:
        if str(temp) not in s:
            ans = temp
            break
        temp += 1
    print(f'#{tt} {ans}')