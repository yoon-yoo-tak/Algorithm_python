"""

9455 박스

"""



import sys
input = sys.stdin.readline

#
# for _ in range(int(input())):
#     n, m = map(int, input().split())
#     ans = 0
#     ls = [list(map(int, input().split())) for _ in range(n)]
#
#     ls = ls[::-1]
#
#
#     new_ls = [[] * n for _ in range(m)]
#
#
#     for i in range(m):
#         for j in range(n):
#             new_ls[i].append(ls[j][i])
#
#
#     ans = 0
#     for i in new_ls:
#         one_cnt = i.count(1)
#         one_pos = [j for j in range(len(i)) if i[j] == 1]
#         if one_cnt <= 1:
#             ans += sum(one_pos)
#         else:
#             ans += one_pos[0]
#             for j in range(1, len(one_pos)):
#                 ans += one_pos[j] - j
#     print(ans)


for _ in range(int(input())):
    m, n = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(m)]
    cnt = 0
    for i in range(m):
        num = board[i].count(1)
        floor = m - 1
        for j in range(n - 1, -1, -1):
            if board[i][j] == 1:
                cnt += floor - j
                floor -= 1
    print(cnt)


















    #
    # def rotate_90(a):  # 배열 90도 돌리는 함수
    #     row_length = len(a)
    #     col_length = len(a[0])
    #
    #     res = [[0] * row_length for _ in range(col_length)]
    #     for r in range(row_length):
    #         for c in range(col_length):
    #             res[c][row_length - 1 - r] = a[r][c]
    #     return res
    #
    #
    # for _ in range(int(input())):
    #     n, m = map(int, input().split())
    #     ls = rotate_90([list(map(int, input().split())) for _ in range(n)])
    #     ans = 0
    #     for i in ls:
    #         one_cnt = i.count(1)
    #         one_pos = [pos for pos in range(len(i)) if i[pos] == 1]
    #         if one_cnt <= 1:
    #             ans += sum(one_pos)
    #         else:
    #             ans += one_pos[0]
    #             for j in range(1, len(one_pos)):
    #                 ans += one_pos[j] - j
    #     print(ans)
    #
    #