"""
5948 새샘이의 7-3-5 게임

"""


def my_sum(idx, res, cnt):
    if cnt == 3:
        if res not in num_save:
            num_save.append(res)
        return

    for w in range(idx, 7):
        my_sum(w + 1, res + numbers[w], cnt + 1)
    return


T = int(input())

for tc in range(1, 1 + T):
    numbers = list(map(int, input().split()))
    num_save = []

    for q in range(5):
        my_sum(q + 1, numbers[q], 1)

    num_save.sort(reverse=True)

    print('#{} {}'.format(tc, num_save[4]))
