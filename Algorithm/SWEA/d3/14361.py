"""
14361 숫자가 같은 배수
"""
for tt in range(1, int(input()) + 1):
    ls = [0] * 11
    n = int(input())
    mult = [i * n for i in range(2, 10)]
    ans = 'impossible'
    for i in str(n):
        ls[int(i)] += 1
    for i in mult:
        temp = [0] * 11
        for j in str(i):
            temp[int(j)] += 1
        if temp == ls:
            ans = 'possible'
            break

    print(f'#{tt} {ans}')