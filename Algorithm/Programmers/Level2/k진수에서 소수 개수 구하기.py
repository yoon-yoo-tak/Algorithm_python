"""
프로그래머스 레벨 2 - k진수에서 소수 개수 구하기
"""
import math
def is_prime_number(x):
    if x == 1:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


def solution(n, k):
    answer = 0
    s = ''
    while n > 0:
        temp = n % k
        s += str(temp)
        n //= k
    s = s[::-1]
    s = s.split('0')
    s = [int(i) for i in s if i]
    for i in s:
        if is_prime_number(i):
            answer += 1
    return answer

print(solution(437674, 3))