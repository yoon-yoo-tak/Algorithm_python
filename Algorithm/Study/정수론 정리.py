import sys
input = sys.stdin.readline

"""
1. 소수판정 (루트까지만 해본다)
2. 약수 구하기 (소수판정이랑 똑같이 루트까지만 가다가 n % i ==0 이면 (i, n // i)가 약수쌍이다.
 -- > 제곱수는 두번나올수 있다. 그래서 i * i != n이면 출력 시키는 방식으로.
 약수의 개수가 홀수다 == 제곱수다.
 제곱수가 아니면 약수의 개수가 짝수이다.
3. 소인수 분해
 --> 소인수로 루트보다 큰게 없거나 하나있다.
4. 유클리드 호제법
 --> gcd(6, 10) == gcd(6, 10 - 6)
5. 에라토스테네스의 체
 --> 각 수의 가장 작은 소인수를 구할 수도 있다.
6. 1부터 n까지 x의 배수가 몇개? => n // x개
 --> 1~20, 3의 배수 => 20 // 3 => 6개
1, 2, 3, 4, 5, 6, 7, 8, 9
7. n!에 곱해져 있는 소수 p의 개수 구하기

20! 에 곱해져있는 2의 갯수
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
  1   2   1   3   1     2     1     4     1     2

--> 접근방식 약수 뭐시기한다 > 내 배수에대해서 뭐시기 하겠다.

n // p + n // p // p + n // p // p // p + ... 
"""
# 약수 구하기
n = int(input())
for i in range(1, n + 1):
    if i * i >n:
        break
    if n % i == 0:
        print(i)
        if i * i != n:
            print(n // i)

# 소인수 분해 (기능성)
for i in range(2, n + 1):
    while n % i == 0:
        print(i)
        n //= i
# 소인수 분해 (효율성)
x = n
for i in range(2, n + 1):
    if i * i > n:
        break
    while x % i == 0:
        print(i)
        x //= i
if x != 1: # 루트n보다 큰 값을 소인수로 가진다면.
    print(x)

# 유클리드 호제법(약수 빠르게 구하기)
def get_gcd(a, b):
    while a % b != 0:
        x = a % b
        a, b = b, x
    return b

# 최소공배수
# lcm(a, b) == (a // gcd(a, b)) * b  > 오버플로우 방지
# 두수의 곱은 최대공약수 * 최소공배수

# 에라토스테네스의 체
prime = [True for i in range(1000010)]
prime[1] = False
# 기능성
for i in range(2, 1000010):
    if not prime[i]:
        continue
    for j in range(2 * i, 1000010, i):
        prime[j] = False
# 효율성
for i in range(2, 1000010):
    if not prime[i]:
        continue
    for j in range(i * i, 1000010, i):
        prime[j] = False
# 가장 작은 소인수
prime = [i for i in range(1000010)]
for i in range(2, 1000010):
    if prime[i] != i:
        continue
    for j in range(i * i, 1000010, i):
        if prime[j] == j:
            prime[j] = i

