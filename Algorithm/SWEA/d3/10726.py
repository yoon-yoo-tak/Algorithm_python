"""
10726 2진수 표현
"""
t = int(input())
for tt in range(1, t + 1):
    a, b = map(int, input().split())
    for i in range(a):
        if not b % 2:
            flag = False
        b //= 2
    else:
        flag = True
    result = 'ON' if flag else 'OFF'
    print(f'#{tt} {result}')
