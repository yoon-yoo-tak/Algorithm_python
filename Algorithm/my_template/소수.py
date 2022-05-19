import math


def is_prime(num):  # num이 소수이면 True 리턴 아니라면 False 리턴
    ls = [True for _ in range(num + 1)]

    # 에라토스 테네스의 체
    for i in range(2, int(math.sqrt(num)) + 1):
        if ls[i]:  # i가 소수인 경우
            #  i를 제외한 모든 i의 배수를 지우기
            j = 2
            while i * j <= num:
                ls[i * j] = False
                j += 1
    return True if ls[num] else False


def prime_until_num(num):  # 2부터 num 까지의 소수 출력
    ls = [True for _ in range(num + 1)]

    # 에라토스 테네스의 체
    for i in range(2, int(math.sqrt(num)) + 1):
        if ls[i]:  # i가 소수인 경우
            #  i를 제외한 모든 i의 배수를 지우기
            j = 2
            while i * j <= num:
                ls[i * j] = False
                j += 1
    for i in range(2, num + 1):
        if ls[i]:
            print(i, end=' ')

print(is_prime(31))
prime_until_num(11)


