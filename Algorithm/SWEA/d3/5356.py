"""
5356 의석이의 세로로 말해요

"""

T = int(input())
for tc in range(1, T + 1):
    study = [list(map(str, input())) for _ in range(5)]
    new_arr = [[0] * 15 for _ in range(15)]
    for i in range(len(study)):
        for j in range(len(study[i])):
            new_arr[i][j] = study[i][j]

    ans = ''
    for k in range(15):
        for l in range(15):
            if new_arr[l][k] != 0:
                ans += new_arr[l][k]

    print('#{} {}'.format(tc, ans))