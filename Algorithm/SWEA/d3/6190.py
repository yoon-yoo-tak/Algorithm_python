"""
6190 정곤이의 단조 증가하는 수
"""


# 단조 증가하는 수인지 판단
def check(number):
    num = list(str(number))
    i = 0
    while i < len(num) - 1:
        # 단조 증가하지 않으면 False
        if num[i] > num[i + 1]:
            return False
        i += 1
    return True


T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))
    result = -1

    # A_i * A_j 가 단조증가인지, 최대값인지 판단
    for i in range(N - 1):
        for j in range(i + 1, N):
            num = numbers[i] * numbers[j]
            if result < num and check(num):
                result = num

    print(f'#{test_case} {result}')
