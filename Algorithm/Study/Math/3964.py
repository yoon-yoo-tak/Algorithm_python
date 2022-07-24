"""
3964
"""
import sys
input = sys.stdin.readline

MAX = int(1e6)
primes = []
is_prime = [True] * (MAX + 1)
is_prime[0], is_prime[1] = False, False
for i in range(2, MAX + 1):
    if is_prime[i]:
        primes.append(i)
        for j in range(i ** 2, MAX + 1, i):
            is_prime[j] = False

for _ in range(int(input())):
    n, k = map(int, input().split())
    factorial = []
    ans = int(1e18)
    for p in primes:
        if k % p == 0:
            temp = 0
            while k % p == 0:
                k //= p
                temp += 1
            factorial.append((p, temp))

    if k != 1:
        factorial.append((k, 1))

    for p, e in factorial:
        temp, temp1 = n, 0
        while temp:
            temp1 += temp // p
            temp //= p
        ans = min(ans, temp1 // e)
    print(ans)
