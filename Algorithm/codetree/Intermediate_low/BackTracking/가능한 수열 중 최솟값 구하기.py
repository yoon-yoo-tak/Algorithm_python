"""

"""
import sys

input = sys.stdin.readline

n = int(input())
numbers = [4, 5, 6]
series = []

def is_possible_series():
    # 가능한 연속 부분 수열의 길이 범위를 탐색합니다.
    length = 1
    while True:
        # 연속 부분 수열의 시작과 끝 인덱스를 설정하여 줍니다.
        start1, end1 = len(series) - length, len(series) - 1
        start2, end2 = start1 - length, start1 - 1

        if start2 < 0:
            break

        # 인접한 연속 부분 수열이 같은지 여부를 확인합니다.
        if series[start1:end1 + 1] == series[start2:end2 + 1]:
            return False

        length += 1

    return True

def rec(k):
    if k == n:
        for i in series:
            print(i, end='')
        sys.exit()
    else:
        for i in numbers:
            series.append(i)

            if is_possible_series():
                rec(k + 1)
            series.pop()

rec(0)
