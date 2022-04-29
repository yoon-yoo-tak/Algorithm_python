for t in range(int(input())):
    ans = 'impossible'
    a, b, c, d = map(int, input().split())
    if b == (c + 1):
        ans = '0' * (a + 1) + '1' * (d + 1) + '01' * c
    elif b == c and b != 0:
        ans = '0' * (a + 1) + '1' * (d + 1) + '01' * (c - 1) + '0'
    elif c == (b + 1):
        ans = '1' * (d + 1) + '0' * (a + 1) + '10' * b
    elif a * d == 0:
        if a:
            ans = '0' * (a + 1)
        else:
            ans = '1' * (d + 1)
    print(f'#{t + 1} {ans}')