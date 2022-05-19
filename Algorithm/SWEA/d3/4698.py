"""
4698 테네스의 특별한 소수

"""
import math
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
    return ls

ls = prime_until_num(1000001)

for tt in range(1, int(input()) + 1):
    d, a, b = map(int, input().split())
    ans = 0
    for i in range(a, b + 1):
        if i == 1:
            continue
        if ls[i] and str(d) in str(i):
           ans += 1
    print(f'#{tt} {ans}')