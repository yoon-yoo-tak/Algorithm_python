
prime = []
for i in range(1000001):
    prime.append(True)

for i in range(2,int(1000000**0.5)+1):
    if prime[i] == True:
        for j in range(i*i,1000001,i):
            prime[j] = False
primes = [i for i in range(2,1000001) if prime[i]]


N = int(input())
K = list(map(int,input().split()))

num = 1
for names in K:
    num *= names


prime_factorization = []
k = 2
for i in primes:
    while num%i == 0:
        prime_factorization.append(i)
        num //= i
#소인수 집합
soinsu = sorted(list(set(prime_factorization)))
e = []
for i in soinsu:
    for j in range(prime_factorization.count(i)//N):
        e.append(i)
total = 1
for i in e:
    total = total*i

ans = []
for i in K:
    for j in e:
        if i % j == 0:
            ans.append(0)
            i //= j
        else:
            ans.append(1)
print(total, sum(ans))

