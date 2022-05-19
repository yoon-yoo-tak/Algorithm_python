"""
5549 홀수일까 짝수일까

"""
for tt in range(1, int(input()) + 1):
    s = input()
    if int(s[-1]) % 2 == 0:
        ans = 'Even'
    else:
        ans = 'Odd'

    print(f'#{tt} {ans}')