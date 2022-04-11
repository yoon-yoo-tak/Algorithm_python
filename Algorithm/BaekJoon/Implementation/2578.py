"""
2578 빙고

"""

import sys

input = sys.stdin.readline
bingo = [list(map(int, input().split())) for _ in range(5)]
board = [[False] * 5 for _ in range(5)]
cnt = 0

for _ in range(3):
    ls = list(map(int, input().split()))
    for item in ls:
        ans = 0
        cnt += 1
        for i in range(5):
            for j in range(5):
                if bingo[i][j] == item:
                    bingo[i][j] = 0

        for i in bingo:
            if sum(i) == 0:
                ans += 1
                print(ans,'번째 가로 추가', cnt,'번째')
                break

        for i in range(5):
            col_sum = 0
            for j in range(5):
                col_sum += bingo[j][i]
            if col_sum == 0:
                ans += 1
                print(ans, '번째 세로 추가', i + 1, '번째 세로 줄')
        tmp_sum = 0
        for i in range(5):
            tmp_sum += bingo[i][i]
        if tmp_sum == 0:
            ans += 1
            print(ans, '번째 오른아래대각선 추가', cnt, '번째')
        tmp_sum2 = 0
        for i in range(5):
            for j in range(4, -1, -1):
                tmp_sum2 += bingo[i][j]
        if tmp_sum2 == 0:
            ans += 1
            print(ans, '번째 왼아래대각선 추가', cnt, '번째')
        if ans >= 3:
            print(cnt)
            sys.exit()